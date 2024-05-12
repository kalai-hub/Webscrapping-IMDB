# It will navigate from home page to the top 250 movies page using selenium
# and then scrap the data.

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
import time

# URL for homepage of IMDB
URL = "https://m.imdb.com/?ref_=nv_home"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

menu = driver.find_element(By.XPATH, '//*[@id="imdbHeader-navDrawerOpen"]/span')
menu.click()

time.sleep(1)

top_250 = driver.find_element(By.XPATH, '//*[@id="imdbHeader"]/div[2]/aside[1]/div/div[2]/div/div[1]/span/div/div/ul/a[2]/span')
top_250.click()

html_source = driver.page_source

html = BeautifulSoup(html_source, "html.parser")

serial_no = [num for num in range(1, 251)]
title_all = html.find_all(name="h3", class_='ipc-title__text')

titles = [title.text.split(" ", maxsplit=1)[1] for title in title_all[1:251]]

year_all = html.find_all(name="div", class_='cli-title-metadata')
years = [year.text[0:4] for year in year_all]

rating_all = html.find_all(name='span', class_='ratingGroup--imdb-rating')
ratings = [rating.text[0:3] for rating in rating_all]

dict = {"S.No": serial_no, "Movie Name": titles, "Year Released": years, "Rating": ratings}

df = pd.DataFrame(dict)
df.to_csv("IMDB Practice.csv", index=False)
df.to_json("IMDB Practice.json", orient="index")