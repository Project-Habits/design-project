// Basic sidebar functionality
const openbtn = document.querySelector(".openbtn");
const sidebarBtn = document.getElementById("sidebarBtn");

function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}
sidebarBtn.addEventListener("click", () => {
  if (sidebarBtn.classList.contains("closebtn")) {
    closeNav();
  } else {
    openNav();
  }
  sidebarBtn.classList.toggle("closebtn");
});
