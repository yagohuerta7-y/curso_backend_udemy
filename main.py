from fastapi import FastAPI

app = FastAPI(title="BD del almacen")

# Definimos la variable con los datos
productos = [
    {"id": 1, "name": "Sandia", "cantidad": 5, "precio": 25},
    {"id": 2, "name": "Mango", "cantidad": 12, "precio": 15},
    {"id": 3, "name": "Manzana", "cantidad": 50, "precio": 8},
    {"id": 4, "name": "Piña", "cantidad": 8, "precio": 30},
    {"id": 5, "name": "Platano", "cantidad": 24, "precio": 5}
]

@app.get("/Home", tags=["Home"])
def home():
    return {'message': 'Bienvenido a la BD del almacen'}

@app.post("/Productos", tags=["Productos"])
def listar_productos():
    return {"data": productos}