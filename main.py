from fastapi import FastAPI
app = FastAPI() #tworzenie instancji aplikacji
@app.get("/") #tutaj endpoint
def read_root():
    return {"hello":"world"}
