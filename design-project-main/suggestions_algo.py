def curate_suggestion(user_data):
    suggestion = {
        "workout":{
            
        },
        "meal":{
            "Name":"",
            "Link":""
        }
    }
    if(user_data["workout"]=="Weightlifting"):
        suggestion["workout"].update({"Bench Press":"3x10"})
        suggestion["workout"].update({"Military Press":"3x10"})
        suggestion["workout"].update({"Squats":"3x8"})
    else:
        suggestion["workout"].update({"Jump Rope":"5min"})
        suggestion["workout"].update({"Stairmaster":"20min"})
        suggestion["workout"].update({"Burpees":"2min"})

    if(user_data["meal"]=="Surplus"):
        suggestion["meal"].update({"Name":"Chicken and Rice Dinner"})
        suggestion["meal"].update({"Link":"https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/"})
    else:
        suggestion["meal"].update({"Name":"Turkey Stuffed Peppers Dinner"})
        suggestion["meal"].update({"Link":"https://www.eatingwell.com/recipe/270287/air-fryer-turkey-stuffed-peppers/"})

    return suggestion

user_input1 = {
    "workout": "Cardiovascular",
    "meal": "Surplus"
}
user_input2 = {
    "workout": "Weightlifting",
    "meal": "Surplus"
}
user_input3 = {
    "workout": "Cardiovascular",
    "meal": "Deficit"
}
user_input4 = {
    "workout": "Weightlifting",
    "meal": "Deficit"
}
print(curate_suggestion(user_input1))
print(curate_suggestion(user_input2))
print(curate_suggestion(user_input3))
print(curate_suggestion(user_input4))