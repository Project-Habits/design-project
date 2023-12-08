import asyncio
from datetime import datetime, timedelta
from typing import Optional
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, delete, and_, or_, Table, func

import uvicorn
from fastapi_sqlalchemy import DBSessionMiddleware, db
# import sqlalchemy_cockroachdb

from schema import User as SchemaUser
from schema import Meal as SchemaMeal
from schema import Workout as SchemaWorkout
from schema import User_Meal as SchemaUM
from schema import User_Workout as SchemaUW
from schema import Activity as SchemaActivity

from models import User as ModelUser
from models import Meal as ModelMeal
from models import Workout as ModelWorkout
from models import User_Meal as ModelUM
from models import User_Workout as ModelUW
from models import Activity as ModelActivity

import random


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# DB_URL = "cockroachdb://dev:RSfmvZZIdlguqlhHm_hPEg@project-habits-6464.g8z.cockroachlabs.cloud:26257/project?sslmode=verify-full"
DB_URL="postgresql://postgres:123@localhost:5432/projhabits"
# DB_URL="postgresql://postgres:playerubg209@localhost:5435/projhabits"

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=DB_URL)

class Form(BaseModel):
    username: str
    workout: str
    workoutGoal: str
    mealDiet: str
    mealCalorie: str
    mealGoal: str

class ChecklistUpdate(BaseModel):
    username: str
    type: str
    day: int
    checked: bool

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def start_db():
#     async with database.engine.begin() as conn:
#         await conn.run_sync(database.Base.metadata.create_all)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)    

async def get_the_user(username: str):
    user = db.session.query(ModelUser).filter(ModelUser.username == username).all()
    return user

async def get_the_pass(password: str):
    u_pass = db.session.query(ModelUser).filter(ModelUser.u_password == password).all()
    return u_pass

async def get_meal(mealname: str):
    return db.session.query(ModelMeal).filter(ModelMeal.mealname == mealname).all()

async def get_workout(workoutname: str):
    return db.session.query(ModelWorkout).filter(ModelWorkout.workoutname == workoutname).all()

async def get_activity(activity_id: int):
    return db.session.query(ModelActivity).filter(ModelActivity.activity_id == activity_id).all()

async def get_user_meals(uid: int, username: str):
    # Using SQL statements for execution since it's a multi-table query
    uid = await get_the_user(username)[0].uid
    meals_id = db.session.query(ModelActivity).filter(ModelActivity.uid == uid).with_entities(ModelActivity.mid)
    print(meals_id)
    return meals_id

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


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
class LoginInfo(BaseModel):
    username: str
    password: str


@app.post("/")
def return_status(form: Form):
    # gets user info
    form.username = form.username.replace('"', '')
    db_user = asyncio.run(get_the_user(form.username))[0]
    uid = db_user.uid

    asyncio.run(delete_user_meals(uid))
    asyncio.run(delete_user_workouts(uid))
    # Here is where we would run the algorithm to determine which workout and meal to return

    if(form.mealDiet == "Vegan"):
        if(form.mealCalorie == "<1800"):
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='b', ModelMeal.diet_type=='Vegan')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='l', ModelMeal.diet_type=='Vegan')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='d', ModelMeal.diet_type=='Vegan')).all()
        elif (form.mealCalorie == "~2000"):
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='b', ModelMeal.diet_type=='Vegan')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='l', ModelMeal.diet_type=='Vegan')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='d', ModelMeal.diet_type=='Vegan')).all()
        else:
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='b', ModelMeal.diet_type=='Vegan')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='l', ModelMeal.diet_type=='Vegan')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='d', ModelMeal.diet_type=='Vegan')).all()
    elif (form.mealDiet == "Vegetarian"):
        if(form.mealCalorie == "<1800"):
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='b', ModelMeal.diet_type!='Balanced')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='l', ModelMeal.diet_type!='Balanced')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='d', ModelMeal.diet_type!='Balanced')).all()
        elif (form.mealCalorie == "~2000"):
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='b', ModelMeal.diet_type!='Balanced')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='l', ModelMeal.diet_type!='Balanced')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='d', ModelMeal.diet_type!='Balanced')).all()
        else:
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='b', ModelMeal.diet_type!='Balanced')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='l', ModelMeal.diet_type!='Balanced')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='d', ModelMeal.diet_type!='Balanced')).all()
    else:
        if(form.mealCalorie == "<1800"):
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='b')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='l')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='d')).all()
        elif (form.mealCalorie == "~2000"):
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='b')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='l')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='d')).all()
        else:
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='b')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='l')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='d')).all()

    if(form.workout == "Strength"):
        workoutList = db.session.query(ModelWorkout).filter(ModelWorkout.w_type=='S').all()
        chestList = db.session.query(ModelWorkout).filter(ModelWorkout.section=='Chest').all()
        shouldList = db.session.query(ModelWorkout).filter(ModelWorkout.section=='Shoulders').all()
        triList = db.session.query(ModelWorkout).filter(ModelWorkout.section=='Triceps').all()
        absList = db.session.query(ModelWorkout).filter(ModelWorkout.section=='Abs').all()
        backList = db.session.query(ModelWorkout).filter(ModelWorkout.section=='Back').all()
        biList = db.session.query(ModelWorkout).filter(ModelWorkout.section=='Biceps').all()
        calfList = db.session.query(ModelWorkout).filter(ModelWorkout.section=='Calves').all()
        quadList = db.session.query(ModelWorkout).filter(ModelWorkout.section=='Quads').all()
        hamList = db.session.query(ModelWorkout).filter(ModelWorkout.section=='Hamstrings').all()
        gluteList = db.session.query(ModelWorkout).filter(ModelWorkout.section=='Glutes').all()
    else:
        workoutList = db.session.query(ModelWorkout).filter(ModelWorkout.w_type=='C').all()
    workoutDict = {}
    mealDict = {}
    for i in range(int(form.mealGoal)):
        if(len(bfList)>0):
            randBfIndex = random.randrange(len(bfList))
            bfName = bfList[randBfIndex].mealname
            bfLink = bfList[randBfIndex].link
            bID = bfList[randBfIndex].mid
            bfList.pop(randBfIndex)
        else:
            bfName = "BreakFast Placeholder"
            bfLink = "www.example.com/breakfast"
            bID = "-1"
        if(len(bfList)>0):
            randLunchIndex = random.randrange(len(lunchList))
            lunchName = lunchList[randLunchIndex].mealname
            lunchLink = lunchList[randLunchIndex].link
            lID = lunchList[randLunchIndex].mid
            lunchList.pop(randLunchIndex)
        else:
            lunchName = "Lunch Placeholder"
            lunchLink = "www.example.com/lunch"
        if(len(dinList)>0):
            randDinIndex = random.randrange(len(dinList))
            dinName = dinList[randDinIndex].mealname
            dinLink = dinList[randDinIndex].link
            dID = dinList[randDinIndex].mid
            dinList.pop(randDinIndex)
        else:
            dinName = "Dinner Placeholder"
            dinLink = "www.example.com/dinner"
        mealDict.update({i+1:{
            "Breakfast":{"Name":bfName, "Link": bfLink, "ID":bID}, 
            "Lunch":{"Name":lunchName, "Link":lunchLink, "ID":lID}, 
            "Dinner":{"Name":dinName, "Link":dinLink, "ID":dID}
            }})

    for i in range(int(form.workoutGoal)):
        workoutDict.update({ i+1 : {}})

    if(form.workout == "Strength"):
        if(form.workoutGoal=='1'):
            workoutDict[1].update({"Try Circuit Training!":""})
        if(form.workoutGoal=='2'):
            workoutDict[1].update({chestList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({triList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({backList[random.randrange(3)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({calfList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({quadList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({hamList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({gluteList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
        if(form.workoutGoal=='3'):
            workoutDict[1].update({chestList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({triList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({shouldList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({backList[random.randrange(3)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({absList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({biList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({calfList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({quadList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({hamList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({gluteList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
        if(form.workoutGoal=='4'):
            workoutDict[1].update({chestList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({triList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({shouldList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({backList[random.randrange(3)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({absList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({biList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({calfList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({quadList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({hamList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({gluteList[random.randrange(2)].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[4].update({"Repeat workout from Day 1 or 2":"Alternate weekly:"})
        if(form.workoutGoal=='5'):
            randIndex = random.randrange(2)
            workoutDict[1].update({chestList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({triList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({shouldList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            backRand = random.randrange(3)
            workoutDict[2].update({backList[backRand].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({absList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({biList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({calfList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({quadList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({hamList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({gluteList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            chestList.pop(randIndex)
            triList.pop(randIndex)
            shouldList.pop(randIndex)
            backList.pop(backRand)
            absList.pop(randIndex)

            randIndex = random.randrange(1)
            workoutDict[4].update({chestList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[4].update({triList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[4].update({shouldList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            backRand = random.randrange(2)
            workoutDict[5].update({backList[backRand].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[5].update({absList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[5].update({biList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
        if(form.workoutGoal=='6'):
            randIndex = random.randrange(2)
            workoutDict[1].update({chestList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({triList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({shouldList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            backRand = random.randrange(3)
            workoutDict[2].update({backList[backRand].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({absList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({biList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({calfList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({quadList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({hamList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({gluteList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            chestList.pop(randIndex)
            triList.pop(randIndex)
            shouldList.pop(randIndex)
            backList.pop(backRand)
            absList.pop(randIndex)
            quadList.pop(randIndex)
            gluteList.pop(randIndex)

            randIndex = random.randrange(1)
            workoutDict[4].update({chestList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[4].update({triList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[4].update({shouldList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            backRand = random.randrange(2)
            workoutDict[5].update({backList[backRand].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[5].update({absList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[5].update({biList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[6].update({calfList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[6].update({quadList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[6].update({hamList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[6].update({gluteList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
        if(form.workoutGoal=='7'):
            randIndex = random.randrange(2)
            workoutDict[1].update({chestList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({triList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[1].update({shouldList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            backRand = random.randrange(3)
            workoutDict[2].update({backList[backRand].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({absList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[2].update({biList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({calfList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({quadList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({hamList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[3].update({gluteList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            chestList.pop(randIndex)
            triList.pop(randIndex)
            shouldList.pop(randIndex)
            backList.pop(backRand)
            absList.pop(randIndex)
            quadList.pop(randIndex)
            gluteList.pop(randIndex)

            randIndex = random.randrange(1)
            workoutDict[4].update({chestList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[4].update({triList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[4].update({shouldList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            backRand = random.randrange(2)
            workoutDict[5].update({backList[backRand].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[5].update({absList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[5].update({biList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[6].update({calfList[0].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[6].update({quadList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[6].update({hamList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[6].update({gluteList[randIndex].workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            workoutDict[7].update({"Use today to work on weak areas!":""})
    else:
        for i in range(int(form.workoutGoal)):
            randIndex = random.randrange(len(workoutList))
            workoutDict[i+1].update({workoutList[randIndex].workoutname:str(random.randrange(30,61,5)) + " min"})
            workoutList.pop(randIndex)
        
    exampleOutput = {
        'workout': workoutDict,
        'meal': mealDict
    }
    for meal in mealDict:
        for mealOfDay in mealDict[meal]:
            #print(uid, mealDict[meal][mealOfDay]['ID'], 0, meal)
            asyncio.run(update_single_meal_by_user(uid, mealDict[meal][mealOfDay]['ID'], 0, meal))

    for day in workoutDict:
        for exercise in workoutDict[day]:
            testList = []
            testList = db.session.query(ModelWorkout).filter(ModelWorkout.workoutname==exercise).all()
            if(len(testList)>0):
                asyncio.run(update_single_workout_by_user(uid, testList[0].wid,0,day))
            else:
                asyncio.run(update_single_workout_by_user(uid, 0,0,day))
    return exampleOutput 

async def add_user(user: LoginInfo):
    db_user = ModelUser(username=user.username, u_password=user.password)
    existing_user = await get_the_user(user.username)
    if (len(existing_user) == 0):
        if (user.username != '' and user.password != ''):
            u_id = db.session.query(ModelUser).count() + 1
            print(u_id, user.username, user.password)
            db_user = ModelUser(uid=u_id, username=user.username, u_password=user.password)
            db.session.add(db_user)
            db.session.commit()
            db.session.query()
            return True
        elif user.username == '':
            print("Must enter username")
        else:
            print("Must enter password")
    
    return False

@app.post('/register') # will be used for registering a new user
def register(user: LoginInfo):
    if asyncio.run(add_user(user)):
        return login(user)
    return {'username': '', 'password': '', 'hashedpassword': '', 'workout': '', 'meal': '', 'status': 0}

@app.post("/progress") #used to update checklist
def update_checklist(update: ChecklistUpdate):
    print(update)
    update.username = update.username.replace('"', '')
    db_user = asyncio.run(get_the_user(update.username))[0]
    uid = db_user.uid
    if(update.checked):
        complete = 1
    else:
        complete = 0
    #print(asyncio.run(get_day_workouts_by_user(uid, update.day)))
    if(update.type=='workout'):
        exercises = asyncio.run(get_day_workouts_by_user(uid, update.day))
        for exercise in exercises:
            asyncio.run(update_single_workout_by_user(uid, exercise, complete, update.day))
    else:
        meals = asyncio.run(get_day_meals_by_user(uid, update.day))
        for meal in meals:
            asyncio.run(update_single_meal_by_user(uid, meal, complete, update.day))
    return {}

@app.post("/login")
def login(user: LoginInfo):
    # hashed_password = pwd_context.hash(user.password)
    hashed_password = get_password_hash(user.password)
    # Here you'd want to check for the username in the database and return the data
    # ...
    # Let me know how you guys plan on formatting this data so I can update it in the JS accordingly
    # Normally you would add another condition below like hashed_password = whatever you get from the database
    # I imagine that if we don't have an account, it would just return empty strings for each of the fields like below, and then everytime we make a change to the data, we would make a call to the database

    valid_user = asyncio.run(get_the_user(user.username))
    valid_pass = asyncio.run(get_the_pass(user.password))
    # get_meals_by_user(SchemaUser(username=user.username, u_password=user.password))
    if (len(valid_user) == 1 and len(valid_pass) == 1):
        print('Login Successful')
        uid = valid_user[0].uid
        mealsList = asyncio.run(get_meals_by_user(uid))
        workoutsList = asyncio.run(get_workouts_by_user(uid))
        #print(db.session.query(ModelUW.a_day).filter(ModelUW.uid == uid).group_by(ModelUW.a_day).order_by(ModelUW.a_day).all())
        mealDays = int(len(db.session.query(ModelUM.a_day).filter(ModelUM.uid == uid).group_by(ModelUM.a_day).order_by(ModelUM.a_day).all()))
        workoutDays = int(len(db.session.query(ModelUW.a_day).filter(ModelUW.uid == uid).group_by(ModelUW.a_day).order_by(ModelUW.a_day).all()))
        mealsDict = {}
        workoutsDict = {}
        for day in range(mealDays):
            mealsDict.update({ day+1 : {}})
        for day in range(workoutDays):
            workoutsDict.update({day+1:{}})

        for mealIndex in range(len(mealsList)):
            meal = db.session.query(ModelMeal).filter(ModelMeal.mid == mealsList[mealIndex]).first()
            status = db.session.query(ModelUM).filter(and_(ModelUM.mid == mealsList[mealIndex],ModelUM.uid==uid)).first()
            mealsDict[status.a_day].update({"Completed": status.complete})
            if(meal.m_type=='b'):
                mealsDict[status.a_day].update({'Breakfast':{"Name":meal.mealname, "Link": meal.link}})
            if(meal.m_type=='l'):
                mealsDict[status.a_day].update({'Lunch':{"Name":meal.mealname, "Link": meal.link}})
            if(meal.m_type=='d'):
                mealsDict[status.a_day].update({'Dinner':{"Name":meal.mealname, "Link": meal.link}})
        #print(mealsDict)
        for wIndex in range(len(workoutsList)):
            workout = db.session.query(ModelWorkout).filter(ModelWorkout.wid == workoutsList[wIndex]).first()
            status = db.session.query(ModelUW).filter(and_(ModelUW.wid == workoutsList[wIndex],ModelUW.uid==uid)).first()
            #print(workout.workoutname, status.a_day,uid)
            #print(status)
            if(workoutsList[wIndex]!=0):
                if(workout.w_type=='C'):
                    workoutsDict[status.a_day].update({"Completed": status.complete})
                    workoutsDict[status.a_day].update({workout.workoutname:str(random.randrange(30,61,5)) + " min"})
                else:
                    workoutsDict[status.a_day].update({"Completed": status.complete})
                    workoutsDict[status.a_day].update({workout.workoutname:str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))})
            elif (workoutDays==4 and status.a_day == 4):
                workoutsDict[status.a_day].update({"Completed": status.complete})
                workoutsDict[4].update({"Repeat workout from Day 1 or 2":"Alternate weekly:"})
            elif (workoutDays==7 and status.a_day == 7):
                workoutsDict[status.a_day].update({"Completed": status.complete})
                workoutsDict[7].update({"Use today to work on weak areas!":""})
            else:
                workoutsDict[status.a_day].update({"Completed": status.complete})
                workoutsDict[1].update({"Try Circuit Training!":""})

        '''for meal in mealsDict:
            print(mealsDict[meal])
        for workout in workoutsDict:
            print(workoutsDict[workout])'''
        #print(mealsDict)
        #print(workoutsDict)         
        example_data = {'username': user.username, 'password': user.password, 'hashedpassword': hashed_password, 
                        'workout': workoutsDict, 'workoutGoal': workoutDays, 'meal': mealsDict, 'mealGoal': mealDays, 'status': 1}

    else:
        print('Login Failed')
        example_data = {'username': '', 'password': '', 'hashedpassword': '', 'workout': '', 'meal': '', 'status': 0}

    return example_data 

@app.get("/")
async def root():
    return {"message": "hello world"}


async def add_activity(user: SchemaUser, meal: SchemaMeal, workout: SchemaWorkout):
    "Update activity table based on what user does."
    curr_user = db.session.query(ModelUser).filter_by(ModelUser.username == user.username)
    curr_meal = db.session.query(ModelMeal).filter_by(ModelMeal.mealname == meal.mealname)
    curr_workout = db.session.query(ModelWorkout).filter_by(ModelWorkout.workoutname == workout.workoutname)
    db_activity = ModelActivity(uid=curr_user.uid, mid=curr_meal.mid, wid=curr_workout.wid, a_day=datetime.today().date())
    db.session.add(db_activity)
    db.session.commit()
    db.session.query()
    return db_activity

async def add_meal(meal: SchemaMeal):
    "Add meal to the catalog of meals in the database.\n\n This makes it so that any user can use these meals."
    db_meal = ModelMeal(mealname=meal.mealname, calories=meal.calories, m_type=meal.m_type, link=meal.link)
    db.session.add(db_meal)
    db.session.commit()
    db.session.query()
    return db_meal

async def add_workout(workout: SchemaWorkout):
    "Add workout to the catalog of workouts in the database.\n\n This makes it so that any user can use these workouts."
    db_workout = ModelWorkout(workoutname=workout.workoutname, calories_burned=workout.calories_burned, w_type=workout.w_type, section=workout.section)
    db.session.add(db_workout)
    db.session.commit()
    db.session.query()
    return db_workout

async def get_mealname_catalog():
    return db.session.query(ModelMeal).filter(ModelMeal.mealname).all()

async def get_meals_by_user(uid: int):
    # Using SQL statements for execution since it's a multi-table query
    meals = db.session.query(ModelUM).filter(ModelUM.uid == uid).all()
    meal_ids = [meal.mid for meal in meals]
    return meal_ids

async def get_day_meals_by_user(uid: int, day: int):
    # Using SQL statements for execution since it's a multi-table query
    meals = db.session.query(ModelUM).filter(and_(ModelUM.uid == uid, ModelUM.a_day==day)).all()
    meal_ids = [meal.mid for meal in meals]
    return meal_ids

async def update_single_meal_by_user(uid: int, mid: int, complete: int, day: int):
    '''
    Updates the 'user_meals' table based on the parameters
    \n
    params:
    -- `uid`: int for logged-in user\n
    - `mid`: int for specific meal
    - `complete`: int that should be `0` for `False` or `1` for `True`
    - `day`: int for the specific day this meal is set for
    '''
    existing_meals = await get_meals_by_user(uid)
    if mid in existing_meals:
        db.session.query(ModelUM).filter(ModelUM.mid == mid, ModelUM.uid == uid).update({ModelUM.complete: complete, ModelUM.a_day: day}, synchronize_session='auto')
    else:
        db_UM = ModelUM(uid=uid, mid=mid, complete=complete, a_day=day)
        db.session.add(db_UM)
    db.session.commit()
    db.session.query()

async def get_workouts_by_user(uid: int):
    # Using SQL statements for execution since it's a multi-table query
    workouts = db.session.query(ModelUW).filter(ModelUW.uid == uid).all()
    workout_ids = [workout.wid for workout in workouts]
    return workout_ids

async def get_day_workouts_by_user(uid: int, day: int):
    # Using SQL statements for execution since it's a multi-table query
    workouts = db.session.query(ModelUW).filter(and_(ModelUW.uid == uid, ModelUW.a_day==day)).all()
    workout_ids = [workout.wid for workout in workouts]
    return workout_ids

async def update_single_workout_by_user(uid: int, wid: int, complete: int, day: int):
    '''
    Updates the 'user_workouts' table based on the parameters
    \n
    params:
    - `uid`: int for logged-in user
    - `wid`: int for specific workout
    - `complete`: int that should be `0` for `False` or `1` for `True`
    - `day`: int for the specific day this workout is set for
    '''
    existing_workouts = await get_workouts_by_user(uid)
    if wid in existing_workouts:
        db.session.query(ModelUW).filter(ModelUW.wid == wid, ModelUW.uid == uid).update({ModelUW.complete: complete, ModelUW.a_day: day}, synchronize_session='auto')
    else:
        db_UW = ModelUW(uid=uid, wid=wid, complete=complete, a_day=day)
        db.session.add(db_UW)
    db.session.commit()
    db.session.query()

async def delete_user_meals(uid: int):
    db.session.query(ModelUM).filter(ModelUM.uid == uid).delete(synchronize_session='auto')
    db.session.commit()
    db.session.query()

async def delete_user_workouts(uid: int):
    db.session.query(ModelUW).filter(ModelUW.uid == uid).delete(synchronize_session='auto')
    db.session.commit()
    db.session.query()

async def get_workoutname_catalog():
    return db.session.query(ModelWorkout).filter(ModelWorkout.workoutname).all()


@app.get('/user')
async def user():
    user = db.session.query(ModelUser).all()
    return user


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)