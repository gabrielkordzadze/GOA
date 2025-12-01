// 1) შექმენით სია სადაც შეინახავთ რიცხვებს და შემდეგ გადაუვლით foreach ის საშუალებით და გამოიტანეთ თითოეული რიცხვი სიიდან
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

numbers.forEach(num => {
  console.log(num);
});


// 2) გამოიყენეთ ზემოთ შექმნილი სია და კონსოლში გამოიტანეთ ამ რიცხვების კვადრატი 
numbers.forEach(num => {
  console.log(num * num);
});


// 3) შექმენით სახელების სია სადაც შეინახავთ თქვენთვის სასურველ სახელებს შემდეგ ამ სიას გადაუარეთ foreach ის საშუალებით და კონსოლში დაბეჭდეთ "hello 'name' " 
const names = ["Anna", "Bob", "Charlie", "Diana"];

names.forEach(name => {
  console.log(`Hello ${name}`);
});


// 4) ზემოთ შექმნილი რიცხვების სიიდან foreach ის საშუალებით გადაუარეთ ამ სიას და კონსოლში დააბრუნეთ ელემენტებისა და ინდექსების ჯამი 
numbers.forEach((num, index) => {
  console.log(num + index);
});


// 5) შექმენით ცვლადი სადაც შეინახავთ ცხოველებს და გამოიტანეთ რომელ ინდექსზე რომელი ცხოველი დგას 
const animals = ["Cat", "Dog", "Elephant", "Lion"];

animals.forEach((animal, index) => {
  console.log(`Index ${index}: ${animal}`);
});


// 6) შექმენით სია სადაც შეინახავთ ობიექტებს (animal, sound.  key/values) შემდეგ გადაუარეთ ამ სიას foreach'ის საშუალებით და საიტზე div'სა და p'ის გამოყენებით გამოსახეთ სიის თითოეული ელემენტი 
const animalSounds = [
  { animal: "Cat", sound: "Meow" },
  { animal: "Dog", sound: "Woof" },
  { animal: "Cow", sound: "Moo" }
];

// body-ში გამომიტანთ სიის ელემენტებს
animalSounds.forEach(item => {
  const div = document.createElement("div"); // div ელემენტი
  const p = document.createElement("p"); // p ელემენტი
  p.textContent = `${item.animal} makes ${item.sound}`;
  div.appendChild(p);
  document.body.appendChild(div);
});
