// 3) შექმენით სარეგისტრაცი ფორმა სადაც გექნებათ ემაილი, პაროლი, სახელი და submit ინფუთი შემდეგ როდესაც მომხმარებელი დააჭერს submit ღილაკს 
// კონსოლში გამოიტანეთ "შენ წარმატებით გაიარე რეგისტრაცია და ასევე მისი მონაცემები რომელიც რეგისტრაციის დროს გამოიყენა"

let form = document.getElementById("registerForm");

form.addEventListener("submit", function(e) {
  e.preventDefault();

  let name = document.getElementById("name").value;
  let email = document.getElementById("email").value;
  let password = document.getElementById("password").value;

  console.log("შენ წარმატებით გაიარე რეგისტრაცია");
  console.log("სახელი:", name);
  console.log("ემაილი:", email);
  console.log("პაროლი:", password);
});
