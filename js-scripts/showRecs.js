// DisplayBut is a button that is used to trigger events like displaying the recommendations
const displayBut = document.getElementById("showRecs");
const cont = document.getElementById("bigCont");
// Using meal element to detect whether or not the cards have been created
let mealEle = document.getElementById("mealCard");

// Helper function to create element when needed w/ class
function createPart(ele, myClass) {
  const myEle = document.createElement(ele);
  myEle.classList.add(myClass);
  return myEle;
}

function mealCard(obj) {
  const cardEle = createPart("div", "cardCont");
  const headerEle = createPart("h1", "cardEle");
  headerEle.textContent = "Meal";
  cardEle.append(headerEle);

  const days = Object.keys(obj);
  days.forEach((day) => {
    const dayEle = createPart("div", "mealDay");
    dayEle.id = "mealDay" + day;
    const dayHeader = createPart("h2", "dayHeader");
    dayHeader.textContent = "Day " + day;
    dayEle.append(dayHeader);
    const keys = Object.keys(obj[day]);
    keys.forEach((key) => {
      const noSpaceKey = key.replace(/\s/g, "");
      const newEle = createPart("h3", noSpaceKey);
      newEle.classList.add("meal");
      newEle.textContent = key;
      dayEle.append(newEle);
      const meals = Object.keys(obj[day][key]);
      meals.forEach((meal) => {
        if (meal == "Completed") {
          // do nothing
        }
        if (meal == "Link") {
          const noSpaceKey = key.replace(/\s/g, "");
          const newEle = createPart("a", noSpaceKey);
          newEle.classList.add("meal");
          newEle.textContent = obj[day][key][meal];
          newEle.href = obj[day][key][meal];
          dayEle.append(newEle);
          return;
        } else if (meal == "Name") {
          const noSpaceKey = key.replace(/\s/g, "");
          const newEle = createPart("p", noSpaceKey);
          newEle.classList.add("meal");
          newEle.textContent = obj[day][key][meal];
          dayEle.append(newEle);
        }
      });
    });
    cardEle.append(dayEle);
  });

  const nameEle = createPart("p", "mealName");
  nameEle.classList.add("meal");
  nameEle.textContent = obj.Name;
  const linkEle = createPart("a", "mealLink");
  linkEle.classList.add("meal");
  linkEle.textContent = obj.Link;
  linkEle.href = obj.Link;

  cardEle.append(nameEle, linkEle);

  cardEle.id = "mealCard";
  return cardEle;
}
function workoutCard(obj) {
  const cardEle = createPart("div", "cardCont");
  const headerEle = createPart("h1", "cardWorkout");
  headerEle.textContent = "Workout";
  cardEle.append(headerEle);
  const days = Object.keys(obj);
  days.forEach((day) => {
    const dayEle = createPart("div", "workDay");
    const dayHeader = createPart("h2", "dayHeader");
    dayHeader.textContent = "Day " + day;
    dayEle.append(dayHeader);
    dayEle.id = "workDay" + day;
    const keys = Object.keys(obj[day]);
    keys.forEach((key) => {
      if (key == "Completed") {
        //do nothing
      } else {
        const noSpaceKey = key.replace(/\s/g, "");
        const newEle = createPart("p", noSpaceKey);
        newEle.classList.add("exercise");
        newEle.textContent = obj[day][key] + " " + key;
        dayEle.append(newEle);
      }
    });
    cardEle.append(dayEle);
  });
  cardEle.id = "workoutCard";
  return cardEle;
}
displayBut.onclick = (event) => {
  event.preventDefault;
  mealEle = document.getElementById("mealCard");
  if (localStorage.getItem("workoutGoal") != null) {
    if (mealEle == null) {
      let workoutObj = JSON.parse(localStorage.getItem("workout"));
      cont.append(workoutCard(workoutObj));
      let mealObj = JSON.parse(localStorage.getItem("meal"));
      cont.append(mealCard(mealObj));
    }
  } else {
  }
};
// If there is user data, trigger the displayBut click event to show the cards
if (localStorage.getItem("workout") != null) {
  displayBut.click();
}
