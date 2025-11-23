import pandas as pd
from Base import Movie, Link, Rating, Ta
#wczytanie plików csv
movies_base = pd.read_csv('movies.csv')
links_base = pd.read_csv('links.csv')
ratings_base = pd.read_csv('ratings.csv')
tags_base = pd.read_csv('tags.csv')

#wstawienie danych do bazy
for _, row in movies_base.iterrows():
    session.add(Movie(movieId=row['movie']))