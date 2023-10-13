const displayBut = document.getElementById('showRecs');
function createPart(ele, myClass) {
  const myEle = document.createElement(ele);
  myEle.classList.add(myClass);
  return myEle
}
displayBut.onclick = (event) => {
  event.preventDefault;
  if (localStorage.getItem('name') != null) {

  }
}
