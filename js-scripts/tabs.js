let overviewTab = document.getElementById('overviewTab');
let workoutTab = document.getElementById('workoutTab');
let mealTab = document.getElementById('mealTab');
overviewTab.addEventListener('click', () => {
  if (!workoutTab.classList.contains('hidden')) {
    console.log('workoutTab not hidden')
  }
  if (!mealTab.classList.contains('hidden')) {
    console.log('mealTab not hidden')
  }
})
