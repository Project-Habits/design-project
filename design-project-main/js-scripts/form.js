// Creating the Form
function formHelper(name, type = 'text', val) {
  const gridRow = document.createElement('div');
  gridRow.classList.add('gridRow');

  const label = document.createElement('label');
  const input = document.createElement('input');
  label.for = name;
  label.innerHTML = name;
  input.id = name;
  input.name = name;
  input.placeholder = name;
  if (type != 'text') {
    input.onfocus = () => {
      input.type = type;
    }
    input.onblur = () => {
      input.type = 'text';
    }
  }

  gridRow.appendChild(input);
  gridRow.appendChild(label);

  return gridRow;
}

function createForm() {
  const formCont = document.createElement('div');
  formCont.classList.add('formCont');
  formCont.classList.add('hidden');
  formCont.setAttribute('val', 22);

  const form = document.createElement('form');
  form.classList.add('cardForm');

  const nameRow = formHelper('Username');
  form.appendChild(nameRow);

  const workoutRow = formHelper('Workout Type');
  form.appendChild(workoutRow);

  const mealRow = formHelper('Meal Goal');
  form.appendChild(mealRow);

  const submitBut = document.createElement('button');
  submitBut.classList.add('submitBut');
  submitBut.innerHTML = "Submit";
  submitBut.setAttribute('type', 'button');
  form.appendChild(submitBut);

  formCont.appendChild(form);
  return formCont;
}

const attachForm = createForm();
document.body.appendChild(attachForm);

const formEle = document.querySelector("div[val]");
const mainEle = document.querySelector(".main");

document.querySelector(".createTask").onclick = (event) => {
  formEle.classList.toggle('hidden');
  document.querySelector(".main").classList.toggle('blur');
  event.stopPropagation();
}
document.querySelector(".main").onclick = () => {
  if (mainEle.classList.contains("blur")) {
    formEle.classList.toggle('hidden');
    document.querySelector(".main").classList.toggle('blur');
  } else {
    // pass
  }
};

