let overviewTab = document.getElementById('overviewTab');
let workoutTab = document.getElementById('workoutTab');
let workoutCard = document.getElementById('workoutCard');
let mealCard = document.getElementById('mealCard');
let mealTab = document.getElementById('mealTab');
let faqBtn = document.getElementById('faqTab')
let faq = document.getElementById('faqPage')
let formBtn = document.getElementById('submitCont')
// try making a function that reassigns these new variables when we click on something 
function reassign() {
  workoutCard = document.getElementById('workoutCard');
  mealCard = document.getElementById('mealCard');
  faqBtn = document.getElementById('faqTab')
  faq = document.getElementById('faqPage')
  formBtn = document.getElementById('submitCont')
}
overviewTab.addEventListener('click', () => {
  reassign();
  setTimeout(() => {
    faqPage.classList.add('hidden');
  }, 350)
  setTimeout(() => {
    submitCont.classList.remove('deleting');
  }, 350)
  setTimeout(() => {
    submitCont.classList.remove('hidden');
  }, 350)
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
  reassign();
  setTimeout(() => {
    faqPage.classList.add('hidden');
  }, 350)
  setTimeout(() => {
    submitCont.classList.remove('deleting');
  }, 350)
  setTimeout(() => {
    submitCont.classList.remove('hidden');
  }, 350)
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
  reassign();
  setTimeout(() => {
    faqPage.classList.add('hidden');
  }, 350)
  setTimeout(() => {
    submitCont.classList.remove('deleting');
  }, 350)
  setTimeout(() => {
    submitCont.classList.remove('hidden');
  }, 350)
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
faqBtn.addEventListener('click', () => {
  setTimeout(() => {
    submitCont.classList.add('deleting');
  }, 150)
  setTimeout(() => {
    submitCont.classList.add('hidden');
  }, 350)
  setTimeout(() => {
    mealCard.classList.add('deleting');
  }, 150)
  setTimeout(() => {
    mealCard.classList.add('hidden');
  }, 350)
  setTimeout(() => {
    workoutCard.classList.add('deleting');
  }, 150)
  setTimeout(() => {
    workoutCard.classList.add('hidden');
  }, 350)
  setTimeout(() => {
    faqPage.classList.remove('hidden');
  }, 350)
})
