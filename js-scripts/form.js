// Creating the Form
function formHelper(name, type = 'text') {
  const gridRow = document.createElement('div');
  gridRow.classList.add('gridRow');

  const label = document.createElement('label');
  const input = document.createElement('input');
  if (name == 'Workout Type') {
    let arr = ["Strength", "Cardiovascular"];
    let selectChoice = document.createElement('select');
    selectChoice.id = 'workoutChoice';
    gridRow.appendChild(selectChoice);

    for (let i = 0; i < arr.length; i++) {
      let option = document.createElement('option');
      option.value = arr[i];
      option.text = arr[i];
      selectChoice.append(option);
    }
    label.innerHTML = name;
  }
  else if (name == 'Meal Type') {
    let arr = ["<1500", "1500-2000", "2000+"];
    let selectChoice = document.createElement('select');
    selectChoice.id = 'mealChoice';
    gridRow.appendChild(selectChoice);

    for (let i = 0; i < arr.length; i++) {
      let option = document.createElement('option');
      option.value = arr[i];
      option.text = arr[i];
      selectChoice.append(option);
    }
    label.innerHTML = name + ' (Calories)';
  } else {

    input.id = name;
    input.name = name;
    if (type != 'text') {
      input.onfocus = () => {
        input.type = type;
      }
      input.onblur = () => {
        input.type = 'text';
      }
    }
    label.innerHTML = name;
    gridRow.appendChild(input);
  }
  label.for = name;
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

  const mealRow = formHelper('Meal Type');
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
