import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alchemy import Base, Movie, Link, Rating, Tag
from main import app, get_db

#
# Używamy in-memory SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# 1. Tworzymy stały silnik testowy
test_engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 2. Tworzymy sesję lokalną opartą na stałym silniku
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


#Tworzy stałe połączenie, tworzy tabele, a po teście zamyka połączenie i czyści.
@pytest.fixture(scope="function")
def session_override():
    # Ustanawia jedno stałe połączenie, aby :memory: było widoczne
    connection = test_engine.connect()

    # Rozpoczyna transakcję (opcjonalnie, ale dobra praktyka)
    transaction = connection.begin()

    # Tworzymy tabele na tym JEDNYM połączeniu
    Base.metadata.create_all(bind=connection)

    # Nadpisujemy funkcję get_db, aby używała testowego połączenia/sesji
    def override_get_db():
        try:
            # Używamy sesji powiązanej ze STAŁYM połączeniem
            db = TestingSessionLocal(bind=connection)
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    # Przekazanie kontroli do testu
    yield

    #Zamykanie i czyszczenie
    transaction.rollback()  # Wycofujemy wszelkie zmiany
    Base.metadata.drop_all(bind=connection)  # Usuwamy tabele
    connection.close()

    # Przywracamy oryginalną zależność get_db
    app.dependency_overrides.pop(get_db)


# Tworzymy klienta testowego
client = TestClient(app)


#YTESTY MOVIES

def test_movies_crud(session_override):  # Używamy fiktury session_override
    """Testuje pełny cykl CRUD dla Filmów."""

    # 1. CREATE
    new_movie_data = {"title": "Test Movie 1", "genres": "Action|Adventure"}
    response = client.post("/movies/", json=new_movie_data)
    assert response.status_code == 201, f"BŁĄD CREATE: Oczekiwano 201, otrzymano {response.status_code}. Treść: {response.text}"

    created_movie = response.json()
    movie_id = created_movie["movieId"]
    assert created_movie["title"] == "Test Movie 1"

    # 2. READ (Lista)
    response = client.get("/movies/")
    assert response.status_code == 200
    movies_list = response.json()
    assert len(movies_list) == 1

    # 2. READ (Pojedynczy)
    response = client.get(f"/movies/{movie_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Movie 1"

    # 3. UPDATE
    update_data = {"title": "Test Movie 1", "genres": "Thriller|Sci-Fi"}
    response = client.put(f"/movies/{movie_id}", json=update_data)
    assert response.status_code == 200, f"BŁĄD UPDATE: Oczekiwano 200, otrzymano {response.status_code}. Treść: {response.text}"
    assert response.json()["genres"] == "Thriller|Sci-Fi"

    # 4. DELETE
    response = client.delete(f"/movies/{movie_id}")
    assert response.status_code == 204

    # Sprawdzenie, czy usunięto
    response = client.get(f"/movies/{movie_id}")
    assert response.status_code == 404


# LINKS

def test_links_crud(session_override):  # Używamy fiktury session_override
    """Testuje pełny cykl CRUD dla Linków."""

    # KROK 0: Utwórz FILM
    movie_data = {"title": "Test Link Movie", "genres": "Test"}
    response_movie = client.post("/movies/", json=movie_data)
    assert response_movie.status_code == 201, f"KROK 0 BŁĄD: Nie udało się utworzyć filmu. Treść: {response_movie.text}"
    movie_id = response_movie.json()["movieId"]

    # Dane testowe
    test_imdb_id = 114709

    # 1. CREATE
    new_links_data = {
        "movieId": movie_id,
        "imdbId": test_imdb_id,
        "tmdbId": 862
    }
    response = client.post("/links/", json=new_links_data)
    assert response.status_code == 201, f"BŁĄD CREATE LINKS: Oczekiwano 201, otrzymano {response.status_code}. Treść: {response.text}"
    created_link = response.json()
    assert created_link["movieId"] == movie_id
    assert created_link["imdbId"] == test_imdb_id

    # 2. READ
    response = client.get(f"/links/{movie_id}")
    assert response.status_code == 200
    read_link = response.json()
    assert read_link["imdbId"] == test_imdb_id

    # 3. UPDATE
    update_data = {"tmdbId": 999999}
    response = client.put(f"/links/{movie_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["tmdbId"] == 999999

    # 4. DELETE
    response = client.delete(f"/links/{movie_id}")
    assert response.status_code == 204

    # Sprawdzenie, czy usunięto
    response = client.get(f"/links/{movie_id}")
    assert response.status_code == 404


# RATINGS

def test_ratings_crud(session_override):  # Używamy fiktury session_override
    """Testuje pełny cykl CRUD dla Ocen."""

    # Utwórz FILM
    movie_data = {"title": "Test Rating Movie", "genres": "Drama"}
    response_movie = client.post("/movies/", json=movie_data)
    assert response_movie.status_code == 201, f"KROK 0 BŁĄD: Nie udało się utworzyć filmu. Treść: {response_movie.text}"
    movie_id = response_movie.json()["movieId"]

    # Dane testowe
    test_user_id = 101
    test_rating_value = 4.5

    # 1. CREATE
    new_rating_data = {
        "userId": test_user_id,
        "movieId": movie_id,
        "rating": test_rating_value
    }
    response = client.post("/ratings/", json=new_rating_data)
    assert response.status_code == 201, f"BŁĄD CREATE RATINGS: Oczekiwano 201, otrzymano {response.status_code}. Treść: {response.text}"
    created_rating = response.json()
    assert created_rating["rating"] == test_rating_value

    # 2. READ
    response = client.get(f"/ratings/{test_user_id}/{movie_id}")
    assert response.status_code == 200
    assert response.json()["rating"] == test_rating_value

    # 3. UPDATE
    new_rating_value = 5.0
    update_data = {"rating": new_rating_value}
    response = client.put(f"/ratings/{test_user_id}/{movie_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["rating"] == new_rating_value

    # 4. DELETE
    response = client.delete(f"/ratings/{test_user_id}/{movie_id}")
    assert response.status_code == 204

    # Sprawdzenie, czy usunięto
    response = client.get(f"/ratings/{test_user_id}/{movie_id}")
    assert response.status_code == 404


# TAGS

def test_tags_crud(session_override):
    """Testuje pełny cykl CRUD dla Tagów."""

    # Utwórz FILM
    movie_data = {"title": "Test Tag Movie", "genres": "Comedy"}
    response_movie = client.post("/movies/", json=movie_data)
    assert response_movie.status_code == 201, f"KROK 0 BŁĄD: Nie udało się utworzyć filmu. Treść: {response_movie.text}"
    movie_id = response_movie.json()["movieId"]

    # Dane testowe
    test_user_id = 202
    test_tag_content = "inspirational"

    # 1. CREATE
    new_tag_data = {
        "userId": test_user_id,
        "movieId": movie_id,
        "tag": test_tag_content
    }
    response = client.post("/tags/", json=new_tag_data)
    assert response.status_code == 201, f"BŁĄD CREATE TAGS: Oczekiwano 201, otrzymano {response.status_code}. Treść: {response.text}"
    created_tag = response.json()
    tag_id = created_tag["id"]
    assert created_tag["tag"] == test_tag_content

    # 2. READ
    response = client.get(f"/tags/{tag_id}")
    assert response.status_code == 200
    assert response.json()["tag"] == test_tag_content

    # 3. UPDATE
    new_tag_content = "feel-good movie"
    update_data = {"tag": new_tag_content}
    response = client.put(f"/tags/{tag_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["tag"] == new_tag_content

    # 4. DELETE
    response = client.delete(f"/tags/{tag_id}")
    assert response.status_code == 204

    # Sprawdzenie, czy usunięto
    response = client.get(f"/tags/{tag_id}")
    assert response.status_code == 404