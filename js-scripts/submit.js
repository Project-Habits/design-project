const submitBut = document.querySelector("button[class='submitBut']");
const formEle = document.querySelector("div[val]");
let userData = {
  table: []
}
submitBut.onclick = async (event) => {
  // Blur background behind the form
  event.preventDefault;
  formEle.classList.toggle('hidden');
  document.querySelector(".main").classList.toggle('blur');
  // Read the form values into variables
  const workoutEntry = formEle.querySelector("input[id='Workout Type?']").value;
  const mealEntry = formEle.querySelector("input[id='Meal Goal?']").value;
  fetch('http://127.0.0.1:8000', {
    method: "POST",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "workout": workoutEntry, "meal": mealEntry }),
  })
    .then(response => response.json())
    .then(data => { console.log(data); })
}
