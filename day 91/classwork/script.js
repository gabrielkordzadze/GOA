// ვპოულობთ ღილაკს მისი ID-ით
const loginButton = document.getElementById('loginBtn');

// ვამატებთ ღილაკს click მოვლენა
loginButton.addEventListener('click', function () {
  // ვიღებთ ინფუთებიდან მნიშვნელობებს
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // თუ ცარიელია რომელიმე ველი
  if (username === "" || password === "") {
    alert("გთხოვთ შეავსოთ ყველა ველი!");
    return;
  }

  // კონსოლში გამოტანა
  console.log(" Username/Email:", username);
  console.log(" Password:", password);

  // შეტყობინება
  alert("შესვლა წარმატებულია! (Console-ში წერია მონაცემები)");
});
