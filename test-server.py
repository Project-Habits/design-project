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
    exampleWorkout = { "Bench Press": "3x10", "Military Press": "3x10", "Squats": "3x8" }
    exampleWorkout2 = { "Leg Lifts": "3x10", "Dumbbell Press": "3x10", "Squats": "3x8" }
    exampleBfst = {"Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/"}
    exampleLnch = {"Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/"}
    exampleDin = {"Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/"}
    exampleMeal = {"Breakfast": exampleBfst, "Lunch": exampleLnch, "Dinner": exampleDin}
    exampleMeal2 = {"Breakfast": exampleBfst, "Lunch": exampleLnch, "Dinner": exampleDin}
    oneDayWorkout = {1: exampleWorkout}
    oneDayMeal = {1: exampleMeal}
    twoDayWorkout = {1: exampleWorkout, 2: exampleWorkout2}
    twoDayMeal = {1: exampleMeal, 2: exampleMeal2}
    threeDayWorkout = {1: exampleWorkout, 2: exampleWorkout2, 3: exampleWorkout}
    threeDayMeal = {1: exampleMeal, 2: exampleMeal2, 3: exampleMeal}
    fourDayWorkout = {1: exampleWorkout, 2: exampleWorkout2, 3: exampleWorkout, 4: exampleWorkout}
    fourDayMeal = {1: exampleMeal, 2: exampleMeal2, 3: exampleMeal, 4: exampleMeal}
    fiveDayWorkout = {1: exampleWorkout, 2: exampleWorkout2, 3: exampleWorkout, 4: exampleWorkout, 5: exampleWorkout}
    fiveDayMeal = {1: exampleMeal, 2: exampleMeal2, 3: exampleMeal, 4: exampleMeal, 5: exampleMeal}
    sixDayWorkout = {1: exampleWorkout, 2: exampleWorkout2, 3: exampleWorkout, 4: exampleWorkout, 5: exampleWorkout, 6: exampleWorkout}
    sixDayMeal = {1: exampleMeal, 2: exampleMeal2, 3: exampleMeal, 4: exampleMeal, 5: exampleMeal, 6: exampleMeal}
    sevenDayWorkout = {1: exampleWorkout, 2: exampleWorkout2, 3: exampleWorkout, 4: exampleWorkout, 5: exampleWorkout, 6: exampleWorkout, 7: exampleWorkout}
    sevenDayMeal = {1: exampleMeal, 2: exampleMeal2, 3: exampleMeal, 4: exampleMeal, 5: exampleMeal, 6: exampleMeal, 7: exampleMeal}
    workoutArr = [oneDayWorkout, twoDayWorkout, threeDayWorkout, fourDayWorkout, fiveDayWorkout, sixDayWorkout, sevenDayWorkout]
    mealArr = [oneDayMeal, twoDayMeal, threeDayMeal, fourDayMeal, fiveDayMeal, sixDayMeal, sevenDayMeal]
    example_data = {'workout': workoutArr[int(form.workoutGoal) - 1], 'meal': mealArr[int(form.mealGoal) - 1]}

    return example_data

@app.post("/register")
def register(user: User):
    if user.username == 'new':
        return {'username': '', 'password': '', 'hashedpassword': '', 'workout': '', 'meal': '', 'status': 1}
    else:
        return {'username': '', 'password': '', 'hashedpassword': '', 'workout': '', 'meal': '', 'status': 0}

@app.post("/login")
def login(user: User):
    hashed_password = pwd_context.hash(user.password)
    # Here you'd want to check for the username in the database and return the data
    # ...
    # Let me know how you guys plan on formatting this data so I can update it in the JS accordingly
    # Normally you would add another condition below like hashed_password = whatever you get from the database
    # I imagine that if we don't have an account, it would just return empty strings for each of the fields like below, and then everytime we make a change to the data, we would make a call to the database
    exampleWorkout = {'Completed': 1, "Bench Press": "3x10", "Military Press": "3x10", "Squats": "3x8" }
    exampleWorkout2 = {'Completed': 0, "Leg Lifts": "3x10", "Dumbbell Press": "3x10", "Squats": "3x8" }
    exampleBfst = {"Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/"}
    exampleLnch = {"Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/"}
    exampleDin = {"Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/"}
    exampleMeal = {"Completed": 1, "Breakfast": exampleBfst, "Lunch": exampleLnch, "Dinner": exampleDin}
    exampleMeal2 = {"Completed": 0, "Breakfast": exampleBfst, "Lunch": exampleLnch, "Dinner": exampleDin}
    exampleReturnMeal = {"meal": {1: exampleMeal, 2: exampleMeal2}}
    exampleOutput = {'workout': {1: exampleWorkout, 2: exampleWorkout2}, 'meal': {1: exampleMeal, 2: exampleMeal2}} 
    if (user.username == "test"):
        # This is just an example of what the data would look like
        example_data = {'username': user.username, 'password': user.password, 'hashedpassword': hashed_password, 'workout': {1: exampleWorkout, 2: exampleWorkout2}, 'workoutGoal': 2, 'meal': {1: exampleMeal, 2: exampleMeal2}, 'mealGoal': 2, 'status': 1}
        # example_data = {'username': user.username, 'password': user.password, 'hashedpassword': hashed_password, 'workout': {1: exampleWorkout, 2: exampleWorkout2, 3: exampleWorkout, 4: exampleWorkout, 5: exampleWorkout, 6: exampleWorkout, 7: exampleWorkout}, 'meal': {1: exampleMeal, 2: exampleMeal2, 3: exampleMeal, 4: exampleMeal, 5: exampleMeal, 6: exampleMeal, 7: exampleMeal}, 'status': 1}
    else:
        # TODO: create other cases where the user doesn't exist and one where the password is wrong. below would be for if the password is wrong, as shown by status = 0
        example_data = {'username': '', 'password': '', 'hashedpassword': '', 'workout': '', 'meal': '', 'status': 0}
    return example_data 