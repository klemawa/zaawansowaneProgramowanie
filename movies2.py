from fastapi import FastAPI
import csv

app = FastAPI()
class Movie:
    def __init__(self, movieId, title, genres, imdbId=None, tmdbId=None):
        self.id = movieId
        self.title = title
        self.genres = genres
        self.imdbId = imdbId
        self.tmdbId = tmdbId
        self.ratings = []
        self.tags = []

def load_links():
    links = {}
    with open("links.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            links[row["movieId"]] = {"imdbId": row["imdbId"], "tmdbId": row["tmdbId"]}
    return links

def load_ratings():
    ratings = {}
    with open("ratings.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ratings.setdefault(row["movieId"], []).append({
                "userId": row["userId"],
                "rating": row["rating"],
                "timestamp": row["timestamp"]
            })
    return ratings

def load_tags():
    tags = {}
    with open("tags.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tags.setdefault(row["movieId"], []).append({
                "userId": row["userId"],
                "tag": row["tag"],
                "timestamp": row["timestamp"]
            })
    return tags

@app.get("/movies2")
def get_movies():
    movies_list = []

    links = load_links()
    ratings = load_ratings()
    tags = load_tags()

    with open("movies.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            link_info = links.get(row["movieId"], {"imdbId": None, "tmdbId": None})
            movie = Movie(
                movieId=row["movieId"],
                title=row["title"],
                genres=row["genres"],
                imdbId=link_info["imdbId"],
                tmdbId=link_info["tmdbId"]
            )
            movie.ratings = ratings.get(row["movieId"], [])
            movie.tags = tags.get(row["movieId"], [])
            movies_list.append(movie.__dict__)

    return movies_list