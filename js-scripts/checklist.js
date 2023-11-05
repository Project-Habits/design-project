let workoutChart = document.createElement('canvas');
let workChartObj = ''
let mealChart = document.createElement('canvas');
let mealChartObj = ''
const workCheck = document.getElementById('workCheck')
const mealCheck = document.getElementById('mealCheck')
const testButton = document.createElement('button');
let dog = '';
workCheck.appendChild(workoutChart);
workCheck.appendChild(testButton);
mealCheck.appendChild(mealChart);
let workGoal = localStorage.workoutGoal;
let mealGoal = localStorage.mealGoal;
let current = 1;
if (localStorage.workoutGoal != null) {
  for (let i = 0; i < workGoal; i++) {
    console.log(i);
  }
  workChartObj = new Chart(workoutChart, {
    type: 'doughnut',
    data: {
      labels: ['Workout', 'Remaining'],
      datasets: [{
        label: 'Current workGoal',
        data: [workGoal, 0],
        backgroundColor: [
          'rgb(144, 237, 144)',
          'rgb(144, 237, 144)'
        ]
      },
      {
        label: 'Current progress',
        data: [current, workGoal - current],
        backgroundColor: [
          'rgb(52, 207, 235)',
          'rgb(128, 128, 128)'
        ]
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: false,
        },
      }
    }
  });
} else {
  console.log('dog');
}
testButton.addEventListener('click', () => {
  current += 1
  console.log(current);
  workChartObj.config._config.data.datasets[1].data = [current, workGoal - current];
  workChartObj.update();
})
// let exercises = document.getElementsByClassName('exercise');
// let meal = document.querySelector('.mealName');
// for (let i = 0; i, exercises.length; i++) {
//   exercises[i].addEventListener('click', () => {
//     exercises[i].classList.toggle('strike');
//     meal = document.querySelector('.mealName');
//     console.log(meal);
//   })
// }
// TODO: add checklist elements to index.html (chart, checklist)
// This will involve having a chart that has one dataset with the goal
// and then a second with current progress & remaining in order to display inner circle
// This chart needs to be updated whenever a new submit is sent in, or whenever
// we have workout and meal plans to display
// Plan for this: check if we have it in local storage, then create
// chart if so. Update/create whenever a new submit is made as well
// Step 1: Checklist element in index.html DONE
// Step 2: Make checklist element have checklist based on goal #
// Step 3: Make checklist element have chart
// Step 4: Make it so that it updates whenever submit button is hit
