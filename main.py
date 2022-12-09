from fastapi import FastAPI
import pandas as pd
from querys import *

app = FastAPI()

@app.get('/')
async def read_root():
   return {'asdasffgsgfd'}

@app.on_event('startup')
def startup():
    global amazon, disney, hulu, netflix
    amazon=pd.read_csv("amazonfinal.csv")
    disney=pd.read_csv("disneyfinal.csv")
    hulu=pd.read_csv("hulufinal.csv")
    netflix=pd.read_csv("netflixfinal.csv")

@app.get("/get_max_duration1/({anio},{plataforma},{min})")
async def query1(anio:int,plataforma:str,min:str):
    return get_max_duration1(anio,plataforma,min)

@app.get("/get_count_plataform/{plataforma}")
async def query2(plataforma:str):
    return get_count_plataform(plataforma)

@app.get("/get_listedin/{genero}")
async def query3(genero:str):
    return get_listedin(genero)