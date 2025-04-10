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

''' 
 INSTRUCTIONS TO RUN THE FASTAPI APP:
  # on terminal do: # esto crea el entorno virtual: 
  $cd API
  $pip3 install -r requirements.txt
     
    # 1. Install FastAPI and Uvicorn if you haven't already:
 move to the directory where the app.py file is located and run the command below in the terminal:

    
    #2. Create a virtual environment and activate it: 
# To run the FastAPI app, use the command below in the terminal:
  uvicorn app:app --reload
 
 
    #3 Open google chrome and go to url:  http://127.0.0.1:8000/familia
 
 '''