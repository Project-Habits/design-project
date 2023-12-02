const submitBut = document.querySelector("button[class='submitBut']");
const formEle = document.querySelector("div[val]");
const displayBut = document.getElementById('showRecs');
let userData = {
  table: []
}
async function sendData(workout, workGoal, meal, mealGoal) {
  fetch('http://127.0.0.1:8000', {
    method: "POST",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "workout": workout, "workoutGoal": workGoal, "meal": meal, "mealGoal": mealGoal }),
  })
    .then(response => response.json())
    .then(data => {
      console.log('Input: ' + JSON.stringify({ "workout": workout, "workoutGoal": workGoal, "meal": meal, "mealGoal": mealGoal }));
      localStorage.setItem('workout', JSON.stringify(data.workout))
      localStorage.setItem('meal', JSON.stringify(data.meal))
      console.log('Output (from Python server): ' + JSON.stringify(data));
    })
}
submitBut.onclick = (event) => {
  let mealEle = document.getElementById('mealCard');
  // Blur background behind the form
  event.preventDefault;
  formEle.classList.toggle('hidden');
  document.querySelector(".main").classList.toggle('blur');
  // Read the form values into variables
  const workoutEntry = document.getElementById("workoutChoice").value;
  const mealEntry = document.getElementById("mealChoice").value;
  const workoutGoal = document.getElementById("workoutGoal").value;
  const mealGoal = document.getElementById("mealGoal").value;

  // Send data & fetch response to store in localStorage
  sendData(workoutEntry, workoutGoal, mealEntry, mealGoal);
  localStorage.setItem('workoutGoal', workoutGoal);
  localStorage.setItem('mealGoal', mealGoal);

  // Update recommendations if form is resubmitted
  if (mealEle != null) {
    let workoutEle = document.getElementById('workoutCard');
    workoutEle.classList.add('deleting');
    mealEle = document.getElementById('mealCard');
    mealEle.classList.add('deleting');
    setTimeout(() => {
      mealEle.remove();
      workoutEle.remove();
      displayBut.click();
    }, 150)
  } else {
    setTimeout(() => {
      displayBut.click();
    }, 250)

  }
}