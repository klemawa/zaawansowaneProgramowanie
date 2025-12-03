import pandas as pd
from alchemy import Movie, Link, Rating, Tag, Base, engine, SessionLocal

# Tworzenie tabel (tylko raz)
Base.metadata.create_all(engine)

session = SessionLocal()

# Wczytanie CSV
movies_base = pd.read_csv('movies.csv')
links_base = pd.read_csv('links.csv')
ratings_base = pd.read_csv('ratings.csv')
tags_base = pd.read_csv('tags.csv')

for _, row in movies_base.iterrows():
    if not session.get(Movie, row['movieId']):
        session.add(Movie(movieId=row['movieId'], title=row['title'], genres=row['genres']))

for _, row in links_base.iterrows():
    if not session.get(Link, row['movieId']):
        session.add(Link(movieId=row['movieId'], imdbId=row['imdbId'], tmdbId=row['tmdbId']))

from sqlalchemy import and_
for _, row in ratings_base.iterrows():
    existing_rating = session.query(Rating).filter(
        and_(Rating.userId == row['userId'], Rating.movieId == row['movieId'])
    ).first()
    if not existing_rating:
        session.add(Rating(userId=row['userId'], movieId=row['movieId'], rating=row['rating'], timestamp=row['timestamp']))

for _, row in tags_base.iterrows():
    session.add(Tag(userId=row['userId'], movieId=row['movieId'], tag=row['tag'], timestamp=row['timestamp']))

session.commit()
session.close()

print("Dane załadowane do bazy.")
