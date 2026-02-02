from fastapi import FastAPI

app = FastAPI(title="My firts blog")


@app.get("/home")
def home():
    return {'message': 'Hola, este es mi primer endpoint de yago'}