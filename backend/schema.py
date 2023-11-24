# build a schema using pydantic
from pydantic import BaseModel

class User(BaseModel):
    username: str
    u_password: str

    class Config:
        orm_mode = True

class Meal(BaseModel):
    mealname: str
    calories: int
    m_type: str
    diet_type: str
    link: str

    class Config:
        orm_mode = True

class Workout(BaseModel):
    workoutname: str
    calories_burned: int
    w_type: str
    section: str

    class Config:
        orm_mode = True

class User_Meal(BaseModel):
    uid: int
    mid: int

    class Config:
        orm_mode = True

class User_Workout(BaseModel):
    uid: int
    wid: int

    class Config:
        orm_mode = True
        
class Activity(BaseModel):
    uid: int
    mid: int
    wid: int

    class Config:
        orm_mode = True
