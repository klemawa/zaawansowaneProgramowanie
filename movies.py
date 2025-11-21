from fastapi import FastAPI
import csv
app = FastAPI()

class Movie:
    def __init__(self,movieId, title, genres):
        self.id = movieId
        self.title = title
        self.genres = genres


@app.get("/movies")  # tutaj tworzymy endpoint
def get_movies_from_csv():  #metoda do odczytywania z pliku
    movies = []  #pusta lista
    with open("movies.csv", newline = '', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie = Movie(row["movieId"], row["title"], row["genres"])
            movies.append(movie.__dict__) #tutaj serializacja obiektu do śsłownika
    return movies
