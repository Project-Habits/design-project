const submitBut = document.querySelector("button[class='submitBut']");
const formEle = document.querySelector("div[val]");
let userData = {
  table: []
}
async function sendData(name, workout, meal) {
  let ret;
  fetch('http://127.0.0.1:8000', {
    method: "POST",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "username": name, "workout": workout, "meal": meal }),
  })
    .then(response => response.json())
    .then(data => {
      localStorage.setItem("name", data.username);
      localStorage.setItem("workout", data.workout);
      localStorage.setItem("meal", data.meal);
    })
}
submitBut.onclick = (event) => {
  // Blur background behind the form
  event.preventDefault;
  formEle.classList.toggle('hidden');
  document.querySelector(".main").classList.toggle('blur');
  // Read the form values into variables
  const nameEntry = formEle.querySelector("input[id='Username']").value;
  const workoutEntry = formEle.querySelector("input[id='Workout Type']").value;
  const mealEntry = formEle.querySelector("input[id='Meal Goal']").value;

  console.log(nameEntry);
  console.log(workoutEntry);
  console.log(mealEntry);
  // sendData(nameEntry, workoutEntry, mealEntry);
  // Mocking return json response:
  let mockResponse = {
    workout: { "Bench Press": "3x10", "Military Press": "3x10", "Squats": "3x8" }, meal: { "Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/" }
  }
  console.log(mockResponse);

  // Send data, fetch response

}
