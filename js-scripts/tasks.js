// Get the workout card container element
const workoutCardContainer = document.getElementById("workoutCard");

// Get the number of days from localStorage
const mealGoal = localStorage.getItem("workoutGoal");
const numberOfDays = parseInt(mealGoal);
const buttonRow = document.createElement("div");
buttonRow.classList.add("buttonRow");
workoutCardContainer.children[0].after(buttonRow);

// Create buttons for each day
for (let i = 1; i <= numberOfDays; i++) {
  // Create a button element
  const button = document.createElement("button");
  button.classList.add("styleBtn");
  button.textContent = `Day ${i}`;

  // Append the button to the workout card container
  buttonRow.appendChild(button);
}
