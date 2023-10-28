let overviewTab = document.getElementById('overviewTab');
let workoutTab = document.getElementById('workoutTab');
let workoutCard = document.getElementById('workoutCard');
let mealCard = document.getElementById('mealCard');
let mealTab = document.getElementById('mealTab');
let cardProj = document.getElementById('p7None');
overviewTab.addEventListener('click', () => {
  setTimeout(() => {
    workoutCard.classList.remove('deleting');
    mealCard.classList.remove('deleting');
  }, 150)
  setTimeout(() => {
    workoutCard.classList.remove('transforming');
    mealCard.classList.remove('transforming');
  }, 350)
  setTimeout(() => {
    workoutCard.classList.remove('hidden');
    mealCard.classList.remove('hidden');
  }, 600)
})
workoutTab.addEventListener('click', () => {
  setTimeout(() => {
    mealCard.classList.add('deleting');
  }, 150)
  setTimeout(() => {
    mealCard.classList.add('hidden');
  }, 350)
  setTimeout(() => {
    mealCard.classList.remove('transforming');
  }, 350)
  setTimeout(() => {
    workoutCard.classList.remove('deleting');
  }, 150)
  setTimeout(() => {
    workoutCard.classList.remove('hidden');
  }, 350)
  setTimeout(() => {
    workoutCard.classList.add('transforming');
  }, 400)
})
mealTab.addEventListener('click', () => {
  setTimeout(() => {
    workoutCard.classList.add('deleting');
  }, 150)
  setTimeout(() => {
    workoutCard.classList.add('hidden');
  }, 350)
  setTimeout(() => {
    workoutCard.classList.remove('transforming');
  }, 350)
  setTimeout(() => {
    mealCard.classList.remove('deleting');
  }, 150)
  setTimeout(() => {
    mealCard.classList.remove('hidden');
  }, 350)
  setTimeout(() => {
    mealCard.classList.add('transforming');
  }, 400)
})
