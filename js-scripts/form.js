// Creating the Form
function formHelper(name, type = "text") {
  const gridRow = document.createElement("div");
  gridRow.classList.add("gridRow");

  const label = document.createElement("label");
  const input = document.createElement("input");
  // Create elements of the form with different options
  // TODO: Expand options once database is done
  if (name == "Workout Type") {
    let arr = ["Strength", "Cardiovascular"];
    let selectChoice = document.createElement("select");
    selectChoice.id = "workoutChoice";
    gridRow.appendChild(selectChoice);

    for (let i = 0; i < arr.length; i++) {
      let option = document.createElement("option");
      option.value = arr[i];
      option.text = arr[i];
      selectChoice.append(option);
    }
    label.innerHTML = name;
  } else if (name == "Caloric Goal") {
    let caloriesArr = ["<1800", "~2000", ">2200"];
    let selectChoice = document.createElement("select");
    selectChoice.id = "calorieChoice";
    gridRow.appendChild(selectChoice);

    for (let i = 0; i < caloriesArr.length; i++) {
      let option = document.createElement("option");
      option.value = caloriesArr[i];
      option.text = caloriesArr[i];
      selectChoice.append(option);
    }
    label.innerHTML = name + " (Calories)";
  } else if (name == "Diet Type") {
    let arr = ["No restrictions", "Vegetarian", "Vegan"];
    let selectChoice = document.createElement("select");
    selectChoice.id = "dietChoice";
    gridRow.appendChild(selectChoice);
    
    for (let i = 0; i < arr.length; i++) {
      let option = document.createElement("option");
      option.value = arr[i];
      option.text = arr[i];
      selectChoice.append(option);
    }
    label.innerHTML = "Meal " + name;
  } else if (name == "Workouts per week") {
    let arr = ["1", "2", "3", "4", "5", "6", "7"];
    let selectChoice = document.createElement("select");
    selectChoice.id = "workoutGoal";
    gridRow.appendChild(selectChoice);

    for (let i = 0; i < arr.length; i++) {
      let option = document.createElement("option");
      option.value = arr[i];
      option.text = arr[i];
      selectChoice.append(option);
    }
    label.innerHTML = name + " (Goal)";
  } else if (name == "Protein Content") {
    let arr = ["Low", "Medium", "High"];
    let selectChoice = document.createElement("select");
    selectChoice.id = "proteinChoice";
    gridRow.appendChild(selectChoice);
    
    for (let i = 0; i < arr.length; i++) {
      let option = document.createElement("option");
      option.value = arr[i];
      option.text = arr[i];
      selectChoice.append(option);
    }
    label.innerHTML = name;
  } else if (name == "Meals cooked per week") {
    let arr = ["1", "2", "3", "4", "5", "6", "7"];
    let selectChoice = document.createElement("select");
    selectChoice.id = "mealGoal";
    gridRow.appendChild(selectChoice);

    for (let i = 0; i < arr.length; i++) {
      let option = document.createElement("option");
      option.value = arr[i];
      option.text = arr[i];
      selectChoice.append(option);
    }
    label.innerHTML = name + " (Goal)";
  } else {
    // Styling for input
    input.id = name;
    input.name = name;
    if (type != "text") {
      input.onfocus = () => {
        input.type = type;
      };
      input.onblur = () => {
        input.type = "text";
      };
    }
    label.innerHTML = name;
    gridRow.appendChild(input);
  }
  label.for = name;
  gridRow.appendChild(label);

  return gridRow;
}

function createForm() {
  // Utilizing above function to create all the elements of the form
  const formCont = document.createElement("div");
  formCont.classList.add("formCont");
  formCont.classList.add("hidden");
  formCont.setAttribute("val", 22);

  const form = document.createElement("form");
  form.classList.add("cardForm");

  // TODO: Add titles to the form
  const workoutRow = formHelper("Workout Type");
  form.appendChild(workoutRow);
  const workoutGoal = formHelper("Workouts per week");
  form.appendChild(workoutGoal);

  const dietRow = formHelper("Diet Type");
  form.appendChild(dietRow);
  const calorieRow = formHelper("Caloric Goal");
  form.appendChild(calorieRow);
  const proteinRow = formHelper("Protein Content");
  form.appendChild(proteinRow);
  const mealGoal = formHelper("Meals cooked per week");
  form.appendChild(mealGoal);

  const submitBut = document.createElement("button");
  submitBut.classList.add("submitBut");
  submitBut.innerHTML = "Submit";
  submitBut.setAttribute("type", "button");
  form.appendChild(submitBut);

  formCont.appendChild(form);
  return formCont;
}

// Create form and attach to the document during initialization
const attachForm = createForm();
document.body.appendChild(attachForm);

const formEle = document.querySelector("div[val]");
const mainEle = document.querySelector(".main");

// Event listeners for bringing up form when button is clicked + styling
document.querySelector(".createTask").onclick = (event) => {
  formEle.classList.toggle("hidden");
  document.querySelector(".main").classList.toggle("blur");
  event.stopPropagation();
};
document.querySelector(".main").onclick = () => {
  if (mainEle.classList.contains("blur")) {
    formEle.classList.toggle("hidden");
    document.querySelector(".main").classList.toggle("blur");
  } else {
    // pass
  }
};
