from typing import Union
from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel

class Respuesta(BaseModel):
    message: str

class Cliente(BaseModel):
    id_clientes: int
    nombre: str
    email: str

app = FastAPI()


@app.get("/", response_model=Respuesta)
async def index():
    return {"message": "Fast API"}

@app.get("/clientes/", response_model=List[Cliente])
async def clientes():
    with sqlite3.connect("sql/clientes.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("Select * From clientes")
        response = cursor.fetchall()
        return response

@app.get("/clientes/{id_cliente}", response_model=Cliente)
async def clientes(id_cliente: int):
    with sqlite3.connect("sql/clientes.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(f"Select * From clientes where id_clientes = 1")
        response = cursor.fetchone()
        print(response)
        return response