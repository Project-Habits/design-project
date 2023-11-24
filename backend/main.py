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
from sqlalchemy import select, insert, delete, and_, or_, Table

import uvicorn
from fastapi_sqlalchemy import DBSessionMiddleware, db

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
DB_URL="postgresql://postgres:[db_pass]@[db_host]/projhabits"

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
    workout: str
    workoutGoal: str
    mealDiet: str
    mealProtein: str
    mealCalorie: str
    mealGoal: str

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
    # Here is where we would run the algorithm to determine which workout and meal to return
    if(form.mealCalorie == "<1800"):
        bfName = db.session.query(ModelMeal).filter(ModelMeal.calories<1800).first().mealname
    elif (form.mealCalorie == "~2000"):
        bfName = db.session.query(ModelMeal).filter(ModelMeal.calories==2000).first().mealname
    else:
        bfName = db.session.query(ModelMeal).filter(ModelMeal.calories>2200).first().mealname

    if(form.mealDiet == "Vegan"):
        if(form.mealCalorie == "<1800"):
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='b', ModelMeal.diet_type=='vegan')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='l', ModelMeal.diet_type=='vegan')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='d', ModelMeal.diet_type=='vegan')).all()
        elif (form.mealCalorie == "~2000"):
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='b', ModelMeal.diet_type=='vegan')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='l', ModelMeal.diet_type=='vegan')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='d', ModelMeal.diet_type=='vegan')).all()
        else:
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='b', ModelMeal.diet_type=='vegan')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='l', ModelMeal.diet_type=='vegan')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='d', ModelMeal.diet_type=='vegan')).all()
    elif (form.mealDiet == "Vegetarian"):
        if(form.mealCalorie == "<1800"):
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='b', ModelMeal.diet_type!='any')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='l', ModelMeal.diet_type!='any')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories<1800, ModelMeal.m_type=='d', ModelMeal.diet_type!='any')).all()
        elif (form.mealCalorie == "~2000"):
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='b', ModelMeal.diet_type!='any')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='l', ModelMeal.diet_type!='any')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories==2000, ModelMeal.m_type=='d', ModelMeal.diet_type!='any')).all()
        else:
            bfList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='b', ModelMeal.diet_type!='any')).all()
            lunchList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='l', ModelMeal.diet_type!='any')).all()
            dinList = db.session.query(ModelMeal).filter(and_(ModelMeal.calories>2200, ModelMeal.m_type=='d', ModelMeal.diet_type!='any')).all()
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

    #print(type(db.session.query(ModelWorkout).all()))
    if(form.workout == "Strength"):
        workoutList = db.session.query(ModelWorkout).filter(ModelWorkout.w_type=='S').all()
    else:
        workoutList = db.session.query(ModelWorkout).filter(ModelWorkout.w_type=='C').all()
    randIndex = random.randrange(len(bfList))
    bfName = bfList[randIndex].mealname
    bfLink = bfList[randIndex].link
    randIndex = random.randrange(len(lunchList))
    lunchName = lunchList[randIndex].mealname
    lunchLink = lunchList[randIndex].link
    randIndex = random.randrange(len(dinList))
    dinName = dinList[randIndex].mealname
    dinLink = dinList[randIndex].link
    workoutDict = {}
    mealDict = {}
    for i in range(int(form.mealGoal)):
        mealDict.update({i+1:{"Breakfast":{"Name":bfName, "Link": bfLink}, "Lunch":{"Name":lunchName, "Link":lunchLink}, "Dinner":{"Name":dinName, "Link":dinLink}}})

    print(mealDict)
    for i in range(int(form.workoutGoal)):
        randIndex = random.randrange(len(workoutList))
        workoutDict.update({ i+1 : {workoutList[randIndex].workoutname : str(random.randrange(2,5)) + "x" + str(random.randrange(8,12))}})
        workoutList.pop(randIndex)
    exampleOutput = {
        'workout': workoutDict,
        'meal': mealDict
    }
    return exampleOutput 

async def add_user(user: LoginInfo):
    db_user = ModelUser(username=user.username, u_password=user.password)
    existing_user = await get_the_user(user.username)
    if (len(existing_user) == 0):
        u_id = db.session.query(ModelUser).count() + 1
        print(u_id, user.username, user.password)
        db_user = ModelUser(uid=u_id, username=user.username, u_password=user.password)
        db.session.add(db_user)
        db.session.commit()
        db.session.query()
        return True
    
    return False

@app.post('/register') # will be used for registering a new user
def register(user: LoginInfo):
    if asyncio.run(add_user(user)):
        return login(user)
    print("User already exists!")
    return False

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
        example_data = {'username': user.username, 'password': user.password, 'hashedpassword': hashed_password, 'workout': { "Bench Press": "3x10", "Military Press": "3x10", "Squats": "3x8" }, 'workoutGoal': 1, 'meal': { "Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/"}, 'mealGoal': 4, 'status': 1}

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

async def get_meals_by_user(user: SchemaUser):
    user_id = db.session.query(ModelUser).filter(user.username).uid
    print(user_id)
    return db.session.query(ModelUM).filter(ModelUM.uid == user_id).all()

async def get_workoutname_catalog():
    return db.session.query(ModelWorkout).filter(ModelWorkout.workoutname).all()

async def get_workouts_by_user(user: SchemaUser):
    user_id = db.session.query(ModelUser).filter(user.username).uid
    return db.session.query(ModelUW).filter(ModelUW.uid == user_id).all()

@app.get('/user')
async def user():
    user = db.session.query(ModelUser).all()
    return user


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)