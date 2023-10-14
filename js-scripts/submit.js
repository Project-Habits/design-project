const submitBut = document.querySelector("button[class='submitBut']");
const formEle = document.querySelector("div[val]");
const displayBut = document.getElementById('showRecs');
let userData = {
  table: []
}
async function sendData(name, workout, meal) {
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
      // localStorage.setItem("workout", data.workout);
      // localStorage.setItem("meal", data.meal);
      console.log('Input: ' + JSON.stringify({ "username": name, "workout": workout, "meal": meal }))
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
  const nameEntry = formEle.querySelector("input[id='Username']").value;
  localStorage.setItem('username', nameEntry)
  const workoutEntry = formEle.querySelector("input[id='Workout Type']").value;
  const mealEntry = formEle.querySelector("input[id='Meal Goal']").value;

  // Send data & fetch response to store in localStorage
  sendData(nameEntry, workoutEntry, mealEntry);
  setTimeout(() => {
    displayBut.click();
  }, 250)

  // Update recommendations if form is resubmitted
  if (mealEle != null) {
    console.log('here');
    let workoutEle = document.getElementById('workoutCard');
    workoutEle.classList.add('deleting');
    mealEle = document.getElementById('mealCard');
    mealEle.classList.add('deleting');
    setTimeout(() => {
      mealEle.remove();
      workoutEle.remove();
      displayBut.click();
    }, 150)
  }

  // Mocking return json response:
  // let mockResponse = {
  //   workout: { "Bench Press": "3x10", "Military Press": "3x10", "Squats": "3x8" }, meal: { "Name": "Chicken and Rice dinner", "Link": "https://www.campbells.com/recipes/15-minute-chicken-rice-dinner/" }
  // }
  // console.log(mockResponse);
  // localStorage.setItem('workout', JSON.stringify(mockResponse.workout))
  // localStorage.setItem('meal', JSON.stringify(mockResponse.meal))
  // console.log(JSON.parse(localStorage.getItem('workout')))
  // console.log(JSON.parse(localStorage.getItem('meal')))

}
