const displayBut = document.getElementById('showRecs');
function createPart(ele, myClass) {
  const myEle = document.createElement(ele);
  myEle.classList.add(myClass);
  return myEle
}

function workoutCard(obj) {
  const cardEle = createPart('div', 'cardCont');
  const taskEle = createPart('h1', 'cardWorkout');

  const keys = Object.keys(obj);
  console.log(keys);
  keys.forEach((key) => {
    console.log(obj[key] + ' ' + key);
  })

  // const detailEle = createPart('p', 'cardDetail');
  // detailEle.textContent = detail;
  // cardEle.append(taskEle, detailEle);
  // const cardID = task.replace(/\s/g, "");
  // cardEle.id = cardID;
  // return cardEle;
}
displayBut.onclick = (event) => {
  event.preventDefault;
  if (localStorage.getItem('name') != null) {
    let workoutObj = JSON.parse(localStorage.getItem('workout'));
    console.log(workoutObj);
    workoutCard(workoutObj);

    let mealObj = JSON.parse(localStorage.getItem('meal'));
    console.log(mealObj);
    // card(mealObj);
  } else {
    alert("Please use the form to enter your data (+ button)!")
  }
}
