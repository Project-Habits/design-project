from fastapi import FastAPI
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Form(BaseModel):
    workout: str
    workoutGoal: str
    mealDiet: str
    mealProtein: str
    mealCalorie: str
    mealGoal: str

class User(BaseModel):
    username: str
    password: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def return_status(form: Form):
    # Here is where we would run the algorithm to determine which workout and meal to return
    exampleOutput = {
    'workout': { "Bench Press": "3x10", "Military Press": "3x10", "Squats": "3x8" }, 'meal': { "Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/" }
    }
    return exampleOutput 

@app.post("/login")
def login(user: User):
    hashed_password = pwd_context.hash(user.password)
    # Here you'd want to check for the username in the database and return the data
    # ...
    # Let me know how you guys plan on formatting this data so I can update it in the JS accordingly
    # Normally you would add another condition below like hashed_password = whatever you get from the database
    # I imagine that if we don't have an account, it would just return empty strings for each of the fields like below, and then everytime we make a change to the data, we would make a call to the database
    if (user.username == "test"):
        # This is just an example of what the data would look like
        example_data = {'username': user.username, 'password': user.password, 'hashedpassword': hashed_password, 'workout': { "Bench Press": "3x10", "Military Press": "3x10", "Squats": "3x8" }, 'workoutGoal': 1, 'meal': { "Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/"}, 'mealGoal': 4, 'status': 1}
    else:
        # TODO: create other cases where the user doesn't exist and one where the password is wrong. below would be for if the password is wrong, as shown by status = 0
        example_data = {'username': '', 'password': '', 'hashedpassword': '', 'workout': '', 'meal': '', 'status': 0}
    return example_data 