const displayBut = document.getElementById("showRecs");
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

  const submitBut = document.createElement("button");
  submitBut.classList.add("submitBut");
  submitBut.innerHTML = "Submit";
  submitBut.setAttribute("type", "button");
  submitBut.id = "loginSubmit";
  form.appendChild(submitBut);
  return formCont;
}

async function sendLogin(username, password) {
  console.log("send");
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
      // Try to handle the login here
      console.log(
        "Input: " + JSON.stringify({ username: username, password: password })
      );
      localStorage.setItem("username", JSON.stringify(data.username));
      if (data.status == 1) {
        // Handle login success
        console.log("Login successful");
        loginForm.classList.toggle("hidden");
        loginHeader.classList.toggle("hidden");
        main.classList.toggle("hidden");
        if (data.meal) {
          localStorage.setItem("username", JSON.stringify(data.username));
          localStorage.setItem("meal", JSON.stringify(data.meal));
          localStorage.setItem("workout", JSON.stringify(data.workout));
          localStorage.setItem("meal", JSON.stringify(data.meal));
          localStorage.setItem("workoutGoal", JSON.stringify(data.workoutGoal));
          localStorage.setItem("mealGoal", JSON.stringify(data.mealGoal));
          displayBut.click();
        } else {
          // Do nothing, account data doesn't exist yet.
        }
      } else if (data.status == 0) {
        // Handle login failure
        console.log("Login failed");
        alert("Login failed!");
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
  sendLogin(username, password).then((status) => {
    console.log("here");
  });
};
