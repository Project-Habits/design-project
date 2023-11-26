// TODO: Functionality, add this to a display event listener
// Get the workout card container element
let workoutCardContainer = document.getElementById("workoutCard");
let mealCardContainer = document.getElementById("mealCard");
const submitBut = document.querySelector(".submitBut");
const displayBut = document.getElementById("showRecs");

// Get the number of days from localStorage
const workGoal = localStorage.getItem("workoutGoal");
const workNumberOfDays = parseInt(workGoal);
const workButtonRow = document.createElement("div");
const mealGoal = localStorage.getItem("mealGoal");
const mealNumberOfDays = parseInt(mealGoal);
const mealButtonRow = document.createElement("div");
workButtonRow.classList.add("buttonRow");
workoutCardContainer.children[0].after(workButtonRow);
mealButtonRow.classList.add("buttonRow");
mealCardContainer.children[0].after(mealButtonRow);

function reassign() {
  workoutCardContainer = document.getElementById("workoutCard");
  workoutCardContainer.children[0].after(workButtonRow);
  mealCardContainer = document.getElementById("mealCard");
  mealCardContainer.children[0].after(mealButtonRow);
}
function createButtons() {
  // Get the number of days from localStorage
  const workGoal = localStorage.getItem("workoutGoal");
  const workNumberOfDays = parseInt(workGoal);
  // Add all button
  const workAllButton = document.createElement("button");
  workAllButton.classList.add("styleBtn");
  workAllButton.textContent = "All";
  workAllButton.onclick = () => {
    // Unhide all elements
    const days = document.getElementsByClassName("workDay");
    for (let j = 0; j < days.length; j++) {
      days[j].classList.remove("hidden");
    }
  };
  workButtonRow.appendChild(workAllButton);
  // Create buttons for each day
  for (let i = 1; i <= workNumberOfDays; i++) {
    // Create a button element
    const button = document.createElement("button");
    button.classList.add("styleBtn");
    button.textContent = `Day ${i}`;
    button.onclick = () => {
      // Hide all other elements except the div for that day
      const days = document.getElementsByClassName("workDay");
      for (let j = 0; j < days.length; j++) {
        days[j].classList.add("hidden");
      }
      document.getElementById(`workDay${i}`).classList.remove("hidden");
    };

    // Append the button to the workout card container
    workButtonRow.appendChild(button);
  }
  // Do the same for meal
  const mealGoal = localStorage.getItem("mealGoal");
  const mealNumberOfDays = parseInt(mealGoal);
  // Add allButton
  const mealAllButton = document.createElement("button");
  mealAllButton.classList.add("styleBtn");
  mealAllButton.textContent = "All";
  mealAllButton.onclick = () => {
    // Unhide all elements
    const days = document.getElementsByClassName("mealDay");
    for (let j = 0; j < days.length; j++) {
      days[j].classList.remove("hidden");
    }
  };
  mealButtonRow.appendChild(mealAllButton);
  // Create buttons for each day
  for (let i = 1; i <= mealNumberOfDays; i++) {
    // Create a button element
    const button = document.createElement("button");
    button.classList.add("styleBtn");
    button.textContent = `Day ${i}`;
    button.onclick = () => {
      // Hide all other elements except the div for that day
      const days = document.getElementsByClassName("mealDay");
      for (let j = 0; j < days.length; j++) {
        days[j].classList.add("hidden");
      }
      document.getElementById(`mealDay${i}`).classList.remove("hidden");
    };

    // Append the button to the workout card container
    mealButtonRow.appendChild(button);
  }
}

function updateNumButtons() {
  // If number of buttons in buttonrow (minus all button) is less than the number of days, add buttons
  // Else, remove buttons
  const workGoal = localStorage.getItem("workoutGoal");
  const workNumberOfDays = parseInt(workGoal);
  const mealGoal = localStorage.getItem("mealGoal");
  const mealNumberOfDays = parseInt(mealGoal);
  if (workButtonRow.children.length - 1 < workNumberOfDays) {
    for (let i = workButtonRow.children.length; i <= workNumberOfDays; i++) {
      // Create a button element
      const button = document.createElement("button");
      button.classList.add("styleBtn");
      button.textContent = `Day ${i}`;
      button.onclick = () => {
        // Hide all other elements except the div for that day
        const days = document.getElementsByClassName("workDay");
        for (let j = 0; j < days.length; j++) {
          days[j].classList.add("hidden");
        }
        document.getElementById(`workDay${i}`).classList.remove("hidden");
      };

      // Append the button to the workout card container
      workButtonRow.appendChild(button);
    }
  } else if (workButtonRow.children.length - 1 > workNumberOfDays) {
    for (let i = workButtonRow.children.length - 1; i > workNumberOfDays; i--) {
      workButtonRow.removeChild(workButtonRow.children[i]);
    }
  }
  if (mealButtonRow.children.length - 1 < mealNumberOfDays) {
    for (let i = mealButtonRow.children.length; i <= mealNumberOfDays; i++) {
      // Create a button element
      const button = document.createElement("button");
      button.classList.add("styleBtn");
      button.textContent = `Day ${i}`;
      button.onclick = () => {
        // Hide all other elements except the div for that day
        const days = document.getElementsByClassName("mealDay");
        for (let j = 0; j < days.length; j++) {
          days[j].classList.add("hidden");
        }
        document.getElementById(`mealDay${i}`).classList.remove("hidden");
      };

      // Append the button to the workout card container
      mealButtonRow.appendChild(button);
    }
  } else if (mealButtonRow.children.length - 1 > mealNumberOfDays) {
    for (let i = mealButtonRow.children.length - 1; i > mealNumberOfDays; i--) {
      mealButtonRow.removeChild(mealButtonRow.children[i]);
    }
  }
}

displayBut.addEventListener("click", () => {
  reassign();
  updateNumButtons();
});
createButtons();
