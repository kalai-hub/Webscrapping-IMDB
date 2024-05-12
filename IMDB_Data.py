from selenium import webdriver
from bs4 import BeautifulSoup

# Direct url for top 250 IMDB movies
URL = "https://m.imdb.com/chart/top/"

driver = webdriver.Chrome()
driver.get(URL)
html_source = driver.page_source


class Imdb():
    def __init__(self):
        self.html = BeautifulSoup(html_source, 'html.parser')
        self.movie_name = []
        self.year = []
        self.rating = []
        self.serial_no = [num for num in range(1, 251)]

    def find_data(self):
        name_data = self.html.find_all(name='h3', class_='ipc-title__text')
        name_extract = [name.text for name in name_data]
        movie_names_with_no = name_extract[1:251]
        for movie in movie_names_with_no:
            movie_name_without_no = movie.split(' ', 1)[1]
            self.movie_name.append(movie_name_without_no)
        year_data = self.html.find_all(name='div', class_='cli-title-metadata')
        self.year = [year.text[0:4] for year in year_data]
        rating_data = self.html.find_all(name='span', class_='ratingGroup--imdb-rating')
        self.rating = [rating.text[0:3] for rating in rating_data]

        return [self.serial_no, self.movie_name, self.year, self.rating]
