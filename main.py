from fastapi import FastAPI
from typing import  Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Olá, mundo"}

@app.get("/itens/{item_id}")
def  read_item(item_id: int, q: Optional [str] = None):
    return {"item_id": item_id, "q": q}

#crie uma rota q retorne a soma de dois numeros passados por caminho (path de url)

@app.get("/soma")
async def (a: int, b: int):
    return {"resultado": a + b}

@app.get("/soma/{a}/{b}")
async def (a: int, b: int):
    return {"resultado": a + b}