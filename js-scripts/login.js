function formHelper(name, type = 'text') {
  const gridRow = document.createElement('div');
  gridRow.classList.add('gridRow');

  const label = document.createElement('label');
  const input = document.createElement('input');
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
  const formCont = document.createElement('div');
  formCont.classList.add('formCont');
  formCont.setAttribute('val', 21);
  const form = document.createElement('form');
  form.classList.add('cardForm');

  const username = formHelper('Username');
  form.appendChild(username);

  const password = formHelper('Password', 'password');
  form.appendChild(password);

  formCont.appendChild(form);

  const submitBut = document.createElement('button');
  submitBut.classList.add('submitBut');
  submitBut.innerHTML = "Submit";
  submitBut.setAttribute('type', 'button');
  submitBut.id = 'loginSubmit'
  form.appendChild(submitBut);
  return formCont;
}

async function sendLogin(username, password) {
  fetch('http://127.0.0.1:8000/login', {
    method: "POST",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ "username": username, "password": password }),
  })
    .then(response => response.json())
    .then(data => {
      // localStorage.setItem("meal", data.meal);
      console.log('Input: ' + JSON.stringify({ "username": username, "password": password }))
      localStorage.setItem('username', JSON.stringify(data.username))
      console.log('Output: ' + JSON.stringify(data.username))
      console.log(JSON.stringify(data.status))
      return (JSON.stringify(data.status))
    })
}
const loginForm = createLogin();
document.body.appendChild(loginForm);
const loginSubmit = document.getElementById('loginSubmit');
const loginHeader = document.getElementById('loginHeader');
const main = document.getElementById('main');
loginSubmit.onclick = (event) => {
  event.preventDefault;
  const username = loginForm.querySelector("input[id='Username']").value;
  const password = loginForm.querySelector("input[id='Password']").value;
  sendLogin(username, password);
  loginForm.classList.toggle('hidden');
  loginHeader.classList.toggle('hidden');
  main.classList.toggle('hidden');
}
