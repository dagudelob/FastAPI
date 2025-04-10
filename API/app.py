import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows


@app.get("/numeros")
def get_numeros():
    rows = ["1","2","3","4","69"]
    return rows
    
''' 
 INSTRUCTIONS TO RUN THE FASTAPI APP:
  #1. on terminal do: # esto crea el entorno virtual: 
  move to the directory where the app.py file is located and run the command below in the terminal:
  
    $ cd API
    
  #2. Install FastAPI and Uvicorn if you haven't already / 
      $ pip3 install -r requirements.txt
    
  #3. Create a virtual environment and activate it: // VsCode va a sugerir un entorno virtual, lo aceptas y lo activas
  $ python3 -m venv env
 
   
# To run the FastAPI app, use the command below in the terminal:
  uvicorn app:app --reload
 
 
  #4 Open google chrome and go to url:  http://127.0.0.1:8000/familia
 
 '''
