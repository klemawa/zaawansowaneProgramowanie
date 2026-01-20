from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Result(BaseModel):
    url: str
    person_count: int

@app.post("/results")
def save_result(result: Result):
    print(f"[SERWIS A] Zapisano wynik: ID={result.url}, Osoby={result.person_count}")
    return {"status": "saved"}