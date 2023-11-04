let exercises = document.getElementsByClassName('exercise');
let meal = document.querySelector('.mealName');
for (let i = 0; i, exercises.length; i++) {
  exercises[i].addEventListener('click', () => {
    exercises[i].classList.toggle('strike');
    meal = document.querySelector('.mealName');
    console.log(meal);
  })
}
// TODO: add checklist elements to index.html (chart, checklist)
// This will involve having a chart that has one dataset with the goal
// and then a second with current progress & remaining in order to display inner circle
// This chart needs to be updated whenever a new submit is sent in, or whenever
// we have workout and meal plans to display
