var fs = require('fs');
const submitBut = document.querySelector("button[class='submitBut']");
const formEle = document.querySelector("div[val]");
let userData = {
    table: []
}
submitBut.onclick = (event) => {
  // Blur background behind the form
  event.preventDefault;
  formEle.classList.toggle('hidden');
  document.querySelector(".main").classList.toggle('blur');
  // Read the form values into variables
  const taskEntry = formEle.querySelector("input[id='Workout Type?']").value;
  const projectEntry = formEle.querySelector("input[id='Meal Goal?']").value;
  console.log(taskEntry);
  console.log(projectEntry);
}
userData.table.push({workout: taskEntry, meal: projectEntry});
var json = JSON.stringify(userData);
fs.writeFile("output.json", json, 'utf8', function(err) {
    if (err) throw err;
    console.log('complete');
});