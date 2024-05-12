from IMDB_Data import Imdb
import pandas as pd

Imdb = Imdb()

all_data = Imdb.find_data()

data_dict = {"S.No": all_data[0],
             "Movie Name": all_data[1],
             "Year": all_data[2],
             "Rating": all_data[3]}

df = pd.DataFrame(data_dict)
df.to_csv("Top IMDB Movies.csv", index=False)
df.to_json('Top IMDB Movies.json', orient='index')