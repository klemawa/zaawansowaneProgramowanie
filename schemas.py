from pydantic import BaseModel
from typing import Optional

#movies
class MovieBase(BaseModel):
    title: str
    genres: Optional[str] = None

class MovieCreate(MovieBase):
    pass

class MovieUpdate(MovieBase):
    pass

class MovieOut(MovieBase):
    movieId: int

    class Config:
        from_attributes = True  # <- dla SQLAlchemy ORM

#link
class LinkBase(BaseModel):
    imdbId: Optional[int] = None
    tmdbId: Optional[int] = None

class LinkCreate(LinkBase):
    movieId: int

class LinkUpdate(LinkBase):
    pass

class LinkOut(LinkBase):
    movieId: int

    class Config:
        from_attributes = True

#rating
class RatingBase(BaseModel):
    rating: float
    timestamp: Optional[int] = None

class RatingCreate(RatingBase):
    userId: int
    movieId: int

class RatingUpdate(RatingBase):
    pass

class RatingOut(RatingBase):
    userId: int
    movieId: int

    class Config:
        from_attributes = True

#tags
class TagBase(BaseModel):
    tag: str
    timestamp: Optional[int] = None

class TagCreate(TagBase):
    userId: int
    movieId: int

class TagUpdate(TagBase):
    pass

class TagOut(TagBase):
    id: int
    userId: int
    movieId: int

    class Config:
        from_attributes = True
