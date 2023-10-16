from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Recs(BaseModel):
    username: str
    workout: str
    meal: str
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
@app.post("/")
def return_status(recs: Recs):
    myDict = {
    'workout': { "Bench Press": "3x10", "Military Press": "3x10", "Squats": "3x8" }, 'meal': { "Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/" }
  }
    return myDict
def sendData(data: Recs):
    conn = 0
    try:
        conn = psycopg2.connect(database="postgres", user="postgres", password="Sammydog5!", host="127.0.0.1", port=5432,)
    except:
        print("ur good")
    cur = conn.cursor()
    cur.execute("INSERT INTO DATA (username, workout, meal) VALUES ('"+data["name"]+"','"+data["workout"]+"','"+data["meal"]+"');")
    conn.commit()