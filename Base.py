from sqlalchemy import create_engine, Column, Integer, String,Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, sessionmaker

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    movieId = Column(Integer, primary_key = True)
    title = Column(String, nullable=False)
    genres = Column(String)

    ratings = relationship("Rating", back_populates="movie")
    tags = relationship("Tag", back_populates="movie")
    links = relationship("Link", back_populates="movie", uselist=False)

class Link(Base):
    __tablename__ = 'links'
    movieId = Column(Integer, ForeignKey('movies.movieId'), primary_key = True)
    imdbId = Column(Integer)
    tmdbId = Column(Integer)

    movie = relationship("Movie", back_populates="links")

class Rating(Base):
    __tablename__ = 'ratings'
    userId = Column(Integer, primary_key = True)
    movieId = Column(Integer, ForeignKey('movies.movieId'), primary_key = True)
    rating = Column(Float)
    timestamp = Column(Integer)

    movie = relationship("Movie", back_populates="ratings")

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, nullable=False)
    movieId = Column(Integer, ForeignKey('movies.movieId'), nullable=False)
    tag = Column(String)
    timestamp = Column(Integer)

    movie = relationship("Movie", back_populates="tags")

#tworzenie silnika SQLite
engine = create_engine('sqlite:///movies.db', echo=True)

#tworzenie tabeli w bazie
Base.metadata.create_all(engine)

#tworzenie sesji
Session = sessionmaker(bind=engine)
session = Session()

import pandas as pd

#wczytanie plików csv
movies_base = pd.read_csv('movies.csv')
links_base = pd.read_csv('links.csv')
ratings_base = pd.read_csv('ratings.csv')
tags_base = pd.read_csv('tags.csv')

#wstawienie danych do bazy
for _, row in movies_base.iterrows():
    session.add(Movie(movieId=row['movieId'],title=row['title'],genres=row['genres']))

for _, row in links_base.iterrows():
    session.add(Link(movieId=row['movieId'], imdbId=row['imdbId'], tmdbId=row['tmdbId']))

for _, row in ratings_base.iterrows():
    session.add(Rating(userId=row['userId'], movieId=row['movieId'], rating=row['rating'], timestamp=row['timestamp']))

for _, row in tags_base.iterrows():
    session.add(Tag(userId=row['userId'], movieId=row['movieId'], tag=row['tag'], timestamp=row['timestamp']))

session.commit()
