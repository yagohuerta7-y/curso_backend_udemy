from fastapi import FastAPI, Query

app = FastAPI(title="BD del almacen")

# Definimos la variable con los datos
productos = [
    {"id": 1, "name": "sandia", "cantidad": 5, "precio": 25},
    {"id": 2, "name": "sango", "cantidad": 12, "precio": 15},
    {"id": 3, "name": "manzana", "cantidad": 50, "precio": 8},
    {"id": 4, "name": "piña", "cantidad": 8, "precio": 30},
    {"id": 5, "name": "platano", "cantidad": 24, "precio": 5}
]

@app.get("/Home", tags=["Home"])
def home():
    return {'message': 'Bienvenido a la BD del almacen'}

# Regresamos la lista con todos los productos
@app.get("/Productos", tags=["Productos"])
def listar_productos():
    return {"data": productos}


# Filtrado de resultados usando query params
@app.get("/FiltrarProductos", tags=["Productos"])
def filtrar_productos_por_id(query: int | None = Query(default=None, description="Id del producto que quierees buscar")):
    
    resultado = [producto for producto in productos if producto['id'] == query]
    
    return {"data": resultado}

    # if query is not None:
    #     for producto in productos:
    #         if producto['id'] == query:  
    #             resultado.append(producto)
    #         return {"data": resultado, "Query": query}
    
    
        

            
