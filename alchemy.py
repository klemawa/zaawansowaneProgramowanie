from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    movieId = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genres = Column(String)

    ratings = relationship("Rating", back_populates="movie", cascade="all, delete-orphan")
    tags = relationship("Tag", back_populates="movie", cascade="all, delete-orphan")
    links = relationship("Link", back_populates="movie", uselist=False, cascade="all, delete-orphan")

class Link(Base):
    __tablename__ = 'links'
    movieId = Column(Integer, ForeignKey('movies.movieId'), primary_key=True)
    imdbId = Column(Integer)
    tmdbId = Column(Integer)

    movie = relationship("Movie", back_populates="links")

class Rating(Base):
    __tablename__ = 'ratings'
    userId = Column(Integer, primary_key=True)
    movieId = Column(Integer, ForeignKey('movies.movieId'), primary_key=True)
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


