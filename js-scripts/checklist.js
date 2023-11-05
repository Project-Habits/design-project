// TODO: Fix submit button bug, adding too many checks and not deleting old ones
// TODO: Store progress locally for checklists 
let workoutChart = document.createElement('canvas');
let workChartObj = ''
let mealChart = document.createElement('canvas');
let mealChartObj = ''
const workCheck = document.getElementById('workCheck')
let workList = document.createElement('div');
workList.classList.add('listDiv');
const mealCheck = document.getElementById('mealCheck')
let mealList = document.createElement('div');
mealList.classList.add('listDiv');
let workGoal = localStorage.workoutGoal;
let mealGoal = localStorage.mealGoal;
let workCurrent = 0;
let mealCurrent = 0;
const displayBut = document.getElementById('showRecs');
workCheck.appendChild(workList);
workCheck.appendChild(workoutChart);
mealCheck.appendChild(mealList);
mealCheck.appendChild(mealChart);

function addCheck(num, className) {
  console.log(num);
  let button = document.createElement('button');
  button.classList.add(className);
  let text = document.createElement('h2');
  button.classList.add('checkBtn');
  text.innerHTML = num;
  button.appendChild(text);
  return button
}
function checkButton(button) {
  if (button.firstChild.classList.contains('strike')) {
    button.firstChild.classList.remove('strike');
    return 0
  } else {
    button.firstChild.classList.add('strike');
    return 1
  }
}

displayBut.addEventListener('click', () => {
  workGoal = localStorage.workoutGoal;
  mealGoal = localStorage.mealGoal;
  if (localStorage.workoutGoal != null) {
    for (let i = 1; i <= workGoal; i++) {
      workList.appendChild(addCheck(i, 'workBtn'));
    }
    console.log('not empty');
    let workBtns = document.getElementsByClassName('workBtn');
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
          data: [workCurrent, workGoal - workCurrent],
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
    for (let i = 0; i < workBtns.length; i++) {
      workBtns[i].addEventListener('click', () => {
        if (checkButton(workBtns[i], workCurrent) == 1) {
          workCurrent += 1;
          workChartObj.config._config.data.datasets[1].data = [workCurrent, workGoal - workCurrent];
          workChartObj.update();
        } else {
          workCurrent -= 1;
          workChartObj.config._config.data.datasets[1].data = [workCurrent, workGoal - workCurrent];
          workChartObj.update();
        }
      })
    }
  } else {
    console.log('dog');
  }

  if (localStorage.mealGoal != null) {
    for (let i = 1; i <= mealGoal; i++) {
      mealList.appendChild(addCheck(i, 'mealBtn'));
    }
    let mealBtns = document.getElementsByClassName('mealBtn');
    mealChartObj = new Chart(mealChart, {
      type: 'doughnut',
      data: {
        labels: ['Meal Goal', 'Remaining'],
        datasets: [{
          label: 'Current mealGoal',
          data: [mealGoal, 0],
          backgroundColor: [
            'rgb(144, 237, 144)',
            'rgb(144, 237, 144)'
          ]
        },
        {
          label: 'Current progress',
          data: [mealCurrent, mealGoal - mealCurrent],
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
    for (let i = 0; i < mealBtns.length; i++) {
      mealBtns[i].addEventListener('click', () => {
        if (checkButton(mealBtns[i], mealCurrent) == 1) {
          mealCurrent += 1;
          mealChartObj.config._config.data.datasets[1].data = [mealCurrent, mealGoal - mealCurrent];
          mealChartObj.update();
        } else {
          mealCurrent -= 1;
          mealChartObj.config._config.data.datasets[1].data = [mealCurrent, mealGoal - mealCurrent];
          mealChartObj.update();
        }
      })
    }
  } else {
    console.log('dog');
  }
})
displayBut.click();
