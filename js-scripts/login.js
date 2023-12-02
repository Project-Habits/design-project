// DisplayBut is a button that is used to trigger events like displaying the recommendations
const displayBut = document.getElementById("showRecs");
// Helper function to create a form to be used for logging in
function formHelper(name, type = "text") {
  const gridRow = document.createElement("div");
  gridRow.classList.add("gridRow");

  const label = document.createElement("label");
  const input = document.createElement("input");
  label.for = name;
  label.innerHTML = name;
  input.id = name;
  input.name = name;
  input.type = type;
  input.placeholder = name;

  gridRow.appendChild(input);
  gridRow.appendChild(label);

  return gridRow;
}
export default formHelper;
// Create form
function createLogin() {
  const formCont = document.createElement("div");
  formCont.classList.add("formCont");
  formCont.setAttribute("val", 21);
  const form = document.createElement("form");
  form.classList.add("cardForm");

  const username = formHelper("Username");
  form.appendChild(username);

  const password = formHelper("Password", "password");
  form.appendChild(password);

  formCont.appendChild(form);

  const buttonsRow = document.createElement("div");
  const submitBut = document.createElement("button");
  const registerBut = document.createElement("button");
  registerBut.classList.add("submitBut");
  registerBut.innerHTML = "Register";
  registerBut.setAttribute("type", "button");
  registerBut.id = "loginRegister";
  buttonsRow.appendChild(registerBut);
  submitBut.classList.add("submitBut");
  submitBut.innerHTML = "Submit";
  submitBut.setAttribute("type", "button");
  submitBut.id = "loginSubmit";
  buttonsRow.appendChild(submitBut);
  buttonsRow.classList.add("gridRow");
  buttonsRow.id = "loginButtons";
  formCont.appendChild(buttonsRow);
  return formCont;
}

// Communicate with backend for login
async function sendLogin(username, password) {
  fetch("http://127.0.0.1:8000/login", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username: username, password: password }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle the login here
      console.log(
        "Input: " + JSON.stringify({ username: username, password: password })
      );
      if (data.status == 1) {
        // Handle login success
        loginForm.classList.toggle("hidden");
        loginHeader.classList.toggle("hidden");
        main.classList.toggle("hidden");
        localStorage.clear();
        localStorage.setItem("loggedIn", true);
        console.log("Login successful");
        if (data.meal) {
          localStorage.setItem("username", JSON.stringify(data.username));
          localStorage.setItem("meal", JSON.stringify(data.meal));
          localStorage.setItem("workout", JSON.stringify(data.workout));
          localStorage.setItem("meal", JSON.stringify(data.meal));
          localStorage.setItem("workoutGoal", JSON.stringify(data.workoutGoal));
          localStorage.setItem("mealGoal", JSON.stringify(data.mealGoal));
          displayBut.click();
        } else {
          // Don't store anything , account data doesn't exist yet.
        }
      } else if (data.status == 0) {
        // Handle login failure
        console.log("Login failed");
        alert("Login failed!");
      }
    });
}
async function sendRegister(username, password) {
  fetch("http://127.0.0.1:8000/register", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username: username, password: password }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle the register here
      console.log(
        "Input: " + JSON.stringify({ username: username, password: password })
      );
      if (data.status == 1) {
        // Handle register success
        localStorage.clear();
        console.log("Register successful");
        loginForm.classList.toggle("hidden");
        loginHeader.classList.toggle("hidden");
        main.classList.toggle("hidden");
        // Don't store anything , account data doesn't exist yet.
      } else if (data.status == 0) {
        // Handle register failure
        // TODO: Let me know what to put here for failure.
        console.log("Register failed");
        alert("Register failed!");
      }
    });
}
const loginForm = createLogin();
document.body.appendChild(loginForm);
const loginSubmit = document.getElementById("loginSubmit");
const loginHeader = document.getElementById("loginHeader");
const main = document.getElementById("main");
loginSubmit.onclick = (event) => {
  event.preventDefault;
  const username = loginForm.querySelector("input[id='Username']").value;
  const password = loginForm.querySelector("input[id='Password']").value;
  sendLogin(username, password);
};
loginRegister.onclick = (event) => {
  event.preventDefault;
  const username = loginForm.querySelector("input[id='Username']").value;
  const password = loginForm.querySelector("input[id='Password']").value;
  sendRegister(username, password);
};
if (localStorage.getItem("loggedIn") == "true") {
  loginForm.classList.toggle("hidden");
  loginHeader.classList.toggle("hidden");
  main.classList.toggle("hidden");
  displayBut.click();
}

// Logout functionality
const logoutBut = document.getElementById("logoutBut");
logoutBut.onclick = (event) => {
  event.preventDefault;
  localStorage.clear();
  location.reload();
};
