// 1) click
document.getElementById("btn1").addEventListener("click", function() {
  alert("ღილაკზე დაკლიკდა");
});

// 2) mouseover
document.getElementById("inp2").addEventListener("mouseover", function() {
  this.style.backgroundColor = "lightgreen";
});

// 3) mouseout
document.getElementById("box3").addEventListener("mouseout", function() {
  this.style.backgroundColor = "blue";
});

// 4) keyup
document.getElementById("inp4").addEventListener("keyup", function() {
  console.log("შეიყვანე:", this.value);
});

// 5) dblclick
document.getElementById("btn5").addEventListener("dblclick", function() {
  alert("ღილაკზე ორჯერ დააკლიკე");
});
