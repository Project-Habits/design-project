const displayBut = document.getElementById('showRecs');
const cont = document.getElementById('p7None');
let mealEle = document.getElementById('mealCard');
function createPart(ele, myClass) {
  const myEle = document.createElement(ele);
  myEle.classList.add(myClass);
  return myEle
}

function mealCard(obj) {
  const cardEle = createPart('div', 'cardCont');
  const headerEle = createPart('h1', 'cardEle');
  headerEle.textContent = 'Meal';
  cardEle.append(headerEle);

  const keys = Object.keys(obj);
  console.log(keys);

  const nameEle = createPart('p', 'mealName')
  nameEle.textContent = obj.Name
  const linkEle = createPart('p', 'mealLink')
  linkEle.textContent = obj.Link

  cardEle.append(nameEle, linkEle);

  cardEle.id = 'mealCard';
  return cardEle;
}
function workoutCard(obj) {
  const cardEle = createPart('div', 'cardCont');
  const headerEle = createPart('h1', 'cardWorkout');
  headerEle.textContent = 'Workout';
  cardEle.append(headerEle);

  const keys = Object.keys(obj);
  keys.forEach((key) => {
    const noSpaceKey = key.replace(/\s/g, "");
    const newEle = createPart('p', 'workout' + noSpaceKey)
    newEle.textContent = obj[key] + ' ' + key;
    cardEle.append(newEle);
  })
  cardEle.id = 'workoutCard';
  return cardEle;
}
displayBut.onclick = (event) => {
  event.preventDefault;
  mealEle = document.getElementById('mealCard');
  if (localStorage.getItem('name') != null) {
    if (mealEle == null) {
      let workoutObj = JSON.parse(localStorage.getItem('workout'));
      cont.append(workoutCard(workoutObj));
      let mealObj = JSON.parse(localStorage.getItem('meal'));
      cont.append(mealCard(mealObj));
    }
  } else {
    alert("Please use the form to enter your data (+ button)!")
  }
}
