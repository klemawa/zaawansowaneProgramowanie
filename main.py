from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional  # Poprawka: Dodano import List

# Importujemy Base i wszystkie modele z alchemy.py
from alchemy import Movie, Link, Rating, Tag, Base
from schemas import (
    MovieCreate, MovieUpdate, MovieOut,
    LinkCreate, LinkUpdate, LinkOut,
    RatingCreate, RatingUpdate, RatingOut,
    TagCreate, TagUpdate, TagOut
)


# Plik bazy danych będzie tworzony w katalogu projektu
SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Tworzenie tabel w bazie produkcyjne
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()


def get_db():
    """Zależność do pobierania sesji bazy danych."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/movies/", response_model=MovieOut, status_code=status.HTTP_201_CREATED)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    """Tworzy nowy film."""
    db_movie = Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


@app.get("/movies/", response_model=List[MovieOut])
def read_movies_list(db: Session = Depends(get_db)):
    """Pobiera listę filmów."""
    movies = db.query(Movie).all()
    return movies


@app.get("/movies/{movieId}", response_model=MovieOut)
def read_movie(movieId: int, db: Session = Depends(get_db)):
    """Pobiera pojedynczy film po movieId."""
    movie = db.query(Movie).filter(Movie.movieId == movieId).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@app.put("/movies/{movieId}", response_model=MovieOut)
def update_movie(movieId: int, update: MovieUpdate, db: Session = Depends(get_db)):
    """Aktualizuje istniejący film."""
    movie = db.query(Movie).filter(Movie.movieId == movieId).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    for key, value in update.model_dump(exclude_unset=True).items():
        setattr(movie, key, value)

    db.commit()
    db.refresh(movie)
    return movie


@app.delete("/movies/{movieId}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movieId: int, db: Session = Depends(get_db)):
    """Usuwa film po movieId."""
    movie = db.query(Movie).filter(Movie.movieId == movieId).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(movie)
    db.commit()


# LINKS
@app.post("/links/", response_model=LinkOut, status_code=status.HTTP_201_CREATED)
def create_link(link: LinkCreate, db: Session = Depends(get_db)):
    """Tworzy nowy link dla filmu (wymaga istniejącego movieId)."""
    # Sprawdzenie, czy MovieId istnieje (choć klucz obcy wymusi to w bazie)
    if db.query(Movie).filter(Movie.movieId == link.movieId).first() is None:
        raise HTTPException(status_code=404, detail="Movie not found for this link")

    db_link = Link(**link.model_dump())
    db.add(db_link)
    try:
        db.commit()
        db.refresh(db_link)
        return db_link
    except Exception as e:
        # Obsługa potencjalnego błędu unikalności (jeśli link dla danego movieId już istnieje)
        raise HTTPException(status_code=400,
                            detail="Database error occurred, perhaps link already exists for this movie.")


@app.get("/links/{movieId}", response_model=LinkOut)
def read_link(movieId: int, db: Session = Depends(get_db)):
    """Pobiera link po movieId."""
    link = db.query(Link).filter(Link.movieId == movieId).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link


@app.put("/links/{movieId}", response_model=LinkOut)
def update_link(movieId: int, update: LinkUpdate, db: Session = Depends(get_db)):
    """Aktualizuje link po movieId."""
    link = db.query(Link).filter(Link.movieId == movieId).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")

    for key, value in update.model_dump(exclude_unset=True).items():
        setattr(link, key, value)

    db.commit()
    db.refresh(link)
    return link


@app.delete("/links/{movieId}", status_code=status.HTTP_204_NO_CONTENT)
def delete_link(movieId: int, db: Session = Depends(get_db)):
    """Usuwa link po movieId."""
    link = db.query(Link).filter(Link.movieId == movieId).first()
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    db.delete(link)
    db.commit()


# RATINGS

@app.post("/ratings/", response_model=RatingOut, status_code=status.HTTP_201_CREATED)
def create_rating(r: RatingCreate, db: Session = Depends(get_db)):
    """Tworzy nową ocenę."""
    if db.query(Movie).filter(Movie.movieId == r.movieId).first() is None:
        raise HTTPException(status_code=404, detail="Movie not found for this rating")

    rating = Rating(**r.model_dump())
    db.add(rating)

    try:
        db.commit()
        db.refresh(rating)
        return rating
    except Exception as e:
        # Obsługa błędu, jeśli kombinacja userId/movieId już istnieje (klucz złożony)
        raise HTTPException(status_code=400,
                            detail="Database error occurred, perhaps rating already exists for this user and movie.")


@app.get("/ratings/{userId}/{movieId}", response_model=RatingOut)
def read_rating(userId: int, movieId: int, db: Session = Depends(get_db)):
    """Pobiera ocenę po userId i movieId."""
    rating = db.query(Rating).filter(Rating.userId == userId, Rating.movieId == movieId).first()
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating


@app.put("/ratings/{userId}/{movieId}", response_model=RatingOut)
def update_rating(userId: int, movieId: int, update: RatingUpdate, db: Session = Depends(get_db)):
    """Aktualizuje istniejącą ocenę."""
    rating = db.query(Rating).filter(Rating.userId == userId, Rating.movieId == movieId).first()
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")

    for key, value in update.model_dump(exclude_unset=True).items():
        setattr(rating, key, value)

    db.commit()
    db.refresh(rating)
    return rating


@app.delete("/ratings/{userId}/{movieId}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rating(userId: int, movieId: int, db: Session = Depends(get_db)):
    """Usuwa ocenę po userId i movieId."""
    rating = db.query(Rating).filter(Rating.userId == userId, Rating.movieId == movieId).first()
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    db.delete(rating)
    db.commit()


# TAGS

@app.post("/tags/", response_model=TagOut, status_code=status.HTTP_201_CREATED)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    """Tworzy nowy tag."""
    if db.query(Movie).filter(Movie.movieId == tag.movieId).first() is None:
        raise HTTPException(status_code=404, detail="Movie not found for this tag")

    db_tag = Tag(**tag.model_dump())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


@app.get("/tags/{id}", response_model=TagOut)
def read_tag(id: int, db: Session = Depends(get_db)):
    """Pobiera tag po jego unikalnym ID."""
    tag = db.query(Tag).filter(Tag.id == id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


@app.put("/tags/{id}", response_model=TagOut)
def update_tag(id: int, update: TagUpdate, db: Session = Depends(get_db)):
    """Aktualizuje treść tagu po jego unikalnym ID."""
    tag = db.query(Tag).filter(Tag.id == id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    for key, value in update.model_dump(exclude_unset=True).items():
        setattr(tag, key, value)

    db.commit()
    db.refresh(tag)
    return tag


@app.delete("/tags/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tag(id: int, db: Session = Depends(get_db)):
    """Usuwa tag po jego unikalnym ID."""
    tag = db.query(Tag).filter(Tag.id == id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(tag)
    db.commit()