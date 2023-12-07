// TODO: Store progress in database for checklists
// Create all elements & assign var names to relevant containers
let workoutChart = document.createElement("canvas");
let workChartObj = "";
let mealChart = document.createElement("canvas");
let mealChartObj = "";
const workCheck = document.getElementById("workCheck");
let workList = document.createElement("div");
workList.classList.add("listDiv");
const mealCheck = document.getElementById("mealCheck");
let mealList = document.createElement("div");
mealList.classList.add("listDiv");
let workGoal = localStorage.workoutGoal;
let mealGoal = localStorage.mealGoal;
const displayBut = document.getElementById("showRecs");

// Track current progress
let workCurrent = 0;
let mealCurrent = 0;

// Append to parent element
workCheck.appendChild(workList);
workCheck.appendChild(workoutChart);
mealCheck.appendChild(mealList);
mealCheck.appendChild(mealChart);

// Adding check boxes to checklist cards
function addCheck(num, className) {
  let button = document.createElement("button");
  button.classList.add(className);
  let text = document.createElement("h2");
  button.classList.add("checkBtn");
  text.innerHTML = num;
  button.appendChild(text);
  return button;
}
// Strikethrough if clicked
function checkButton(button) {
  if (button.firstChild.classList.contains("strike")) {
    button.firstChild.classList.remove("strike");
    return 0;
  } else {
    button.firstChild.classList.add("strike");
    return 1;
  }
}

async function sendProgress(username, type, day, checked) {
  fetch("http://127.0.0.1:8000/progress", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    // Send username, workout, and meal data to backend
    body: JSON.stringify({
      username: username,
      type: type,
      day: day,
      checked: checked,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(
        "Input: " +
          JSON.stringify({
            username: username,
            type: type,
            day: day,
            checked: checked,
          })
      );
      console.log("Output (from Python server): " + JSON.stringify(data));
    });
}

// Use displayBut as an event trigger
displayBut.addEventListener("click", () => {
  workGoal = localStorage.workoutGoal;
  mealGoal = localStorage.mealGoal;
  // Using workoutGoal to determine whether or not the user has submitted the form
  // If user data exists, then we want to create the checklists for their tasks
  if (localStorage.workoutGoal != null) {
    let workBtns = document.getElementsByClassName("workBtn");
    let workoutObj = JSON.parse(localStorage.getItem("workout"));
    if (workBtns.length < workGoal) {
      // Reset progress to 0
      workCurrent = 0;
      for (let i = workBtns.length + 1; i <= workGoal; i++) {
        workList.appendChild(addCheck(i, "workBtn"));
        if (workoutObj[i]["Completed"]) {
          workCurrent += 1;
          workList.lastChild.firstChild.classList.add("strike");
        }
      }
    } else if (workBtns.length > workGoal) {
      for (let i = workBtns.length; i > workGoal; i--) {
        workList.removeChild(workList.lastChild);
      }
    }
    workBtns = document.getElementsByClassName("workBtn");
    // Don't want to continously create new charts, so if chart doesn't exist, create chart
    if (!workChartObj.config) {
      workChartObj = new Chart(workoutChart, {
        type: "doughnut",
        data: {
          labels: ["Workout", "Remaining"],
          datasets: [
            {
              label: "Current Workout Goal",
              data: [workGoal, 0],
              backgroundColor: ["rgb(144, 237, 144)", "rgb(144, 237, 144)"],
            },
            {
              label: "Current progress",
              data: [workCurrent, workGoal - workCurrent],
              backgroundColor: ["rgb(52, 207, 235)", "rgb(128, 128, 128)"],
            },
          ],
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              display: false,
            },
          },
        },
      });
    } else {
      // Otherwise just update charts
      workChartObj.config._config.data.datasets[0].data = [workGoal, 0];
      workChartObj.config._config.data.datasets[1].data = [
        workCurrent,
        workGoal - workCurrent,
      ];
      workChartObj.update();
    }
    // Add an event listener for each individual check box
    // If a box is checked, update the chart
    for (let i = 0; i < workBtns.length; i++) {
      let username = localStorage.getItem("username");
      let replaceEle = workBtns[i].cloneNode(true);
      workBtns[i].parentNode.replaceChild(replaceEle, workBtns[i]);
      workBtns[i].addEventListener("click", () => {
        if (checkButton(workBtns[i], workCurrent) == 1) {
          workCurrent += 1;
          workChartObj.config._config.data.datasets[1].data = [
            workCurrent,
            workGoal - workCurrent,
          ];
          sendProgress(username, "workout", i + 1, true);
          workChartObj.update();
        } else {
          workCurrent -= 1;
          workChartObj.config._config.data.datasets[1].data = [
            workCurrent,
            workGoal - workCurrent,
          ];
          sendProgress(username, "workout", i + 1, false);
          workChartObj.update();
        }
      });
    }
  } else {
    // do nothing
  }

  // Same thing as workout goal, but for meals
  if (localStorage.mealGoal != null) {
    let mealBtns = document.getElementsByClassName("mealBtn");
    let mealObj = JSON.parse(localStorage.getItem("meal"));
    if (mealBtns.length < mealGoal) {
      mealCurrent = 0;
      for (let i = mealBtns.length + 1; i <= mealGoal; i++) {
        mealList.appendChild(addCheck(i, "mealBtn"));
        if (mealObj[i]["Completed"]) {
          mealCurrent += 1;
          mealList.lastChild.firstChild.classList.add("strike");
        }
      }
    } else if (mealBtns.length > mealGoal) {
      for (let i = mealBtns.length; i > mealGoal; i--) {
        mealList.removeChild(mealList.lastChild);
      }
    }
    mealBtns = document.getElementsByClassName("mealBtn");
    if (!mealChartObj.config) {
      mealChartObj = new Chart(mealChart, {
        type: "doughnut",
        data: {
          labels: ["Meal Goal", "Remaining"],
          datasets: [
            {
              label: "Current Cooking Goal",
              data: [mealGoal, 0],
              backgroundColor: ["rgb(144, 237, 144)", "rgb(144, 237, 144)"],
            },
            {
              label: "Current progress",
              data: [mealCurrent, mealGoal - mealCurrent],
              backgroundColor: ["rgb(52, 207, 235)", "rgb(128, 128, 128)"],
            },
          ],
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              display: false,
            },
          },
        },
      });
    } else {
      mealChartObj.config._config.data.datasets[0].data = [mealGoal, 0];
      mealChartObj.config._config.data.datasets[1].data = [
        mealCurrent,
        mealGoal - mealCurrent,
      ];
      mealChartObj.update();
    }
    for (let i = 0; i < mealBtns.length; i++) {
      let replaceEle = mealBtns[i].cloneNode(true);
      mealBtns[i].parentNode.replaceChild(replaceEle, mealBtns[i]);
      mealBtns[i].addEventListener("click", () => {
        let username = localStorage.getItem("username");
        if (checkButton(mealBtns[i], mealCurrent) == 1) {
          mealCurrent += 1;
          mealChartObj.config._config.data.datasets[1].data = [
            mealCurrent,
            mealGoal - mealCurrent,
          ];
          sendProgress(username, "meal", i + 1, true);
          mealChartObj.update();
        } else {
          mealCurrent -= 1;
          mealChartObj.config._config.data.datasets[1].data = [
            mealCurrent,
            mealGoal - mealCurrent,
          ];
          sendProgress(username, "meal", i + 1, false);
          mealChartObj.update();
        }
      });
    }
  } else {
    // do nothing
  }
});
displayBut.click();
