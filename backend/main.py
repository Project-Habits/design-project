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
from sqlalchemy import select, insert, delete

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


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url="postgresql://postgres:playerubg209@localhost:5435/projhabits")

class Form(BaseModel):
    workout: str
    workoutGoal: str
    meal: str
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


async def get_user(db: AsyncSession, username: str):
    result = await db.session.query(ModelUser).filter(username=username)
    print(result)
    return result

async def get_the_user(username: str):
    user = db.session.query(ModelUser).filter(ModelUser.username == username).all()
    return user

async def get_the_pass(password: str):
    u_pass = db.session.query(ModelUser).filter(ModelUser.u_password == password).all()
    return u_pass

async def authenticate_user(db: AsyncSession, username: str, password: str):
    user = await get_user(db, username)
    print(user.username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


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
    exampleOutput = {
    'workout': { "Bench Press": "3x10", "Military Press": "3x10", "Squats": "3x8" }, 'meal': { "Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/" }
    }
    return exampleOutput 

@app.post("/login")
def login(user: LoginInfo):
    # hashed_password = pwd_context.hash(user.password)
    hashed_password = get_password_hash(user.password)
    # Here you'd want to check for the username in the database and return the data
    # ...
    # Let me know how you guys plan on formatting this data so I can update it in the JS accordingly
    # Normally you would add another condition below like hashed_password = whatever you get from the database
    # I imagine that if we don't have an account, it would just return empty strings for each of the fields like below, and then everytime we make a change to the data, we would make a call to the database
    # if (user.username == "test"):
    #     # This is just an example of what the data would look like
    #     example_data = {'username': user.username, 'password': user.password, 'hashedpassword': hashed_password, 'workout': { "Bench Press": "3x10", "Military Press": "3x10", "Squats": "3x8" }, 'workoutGoal': 1, 'meal': { "Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/"}, 'mealGoal': 4, 'status': 1}
    # else:
    #     # TODO: create other cases where the user doesn't exist and one where the password is wrong. below would be for if the password is wrong, as shown by status = 0
    #     example_data = {'username': '', 'password': '', 'hashedpassword': '', 'workout': '', 'meal': '', 'status': 0}

    valid_user = asyncio.run(get_the_user(user.username))
    valid_pass = asyncio.run(get_the_pass(user.password))
    
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


@app.post('/user/', response_model=SchemaUser)
async def user(user: SchemaUser):
    db_user = ModelUser(username=user.username, u_password=user.u_password)
    db.session.add(db_user)
    db.session.commit()
    db.session.query()
    return db_user

@app.get('/user/')
async def user():
    user = db.session.query(ModelUser).all()
    return user


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)