// 1. შექმენით ფუნქცია, რომელიც იღებს რიცხვების მასივს და თითოეულ რიცხვს ბეჭდავს for ციკლის გამოყენებით.
function printNumbers(array) {
  for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
  }
}

// მაგალითი
const numbers = [1, 5, 10, 15];
printNumbers(numbers);

// 2. შექმენით სახელების მასივი, შემდეგ, გამოიყენეთ for ციკლი თითოეული სახელის და მისი პოზიციის დასაბეჭდად.
const names = ["Anna", "Bob", "Charlie", "Diana"];

for (let i = 0; i < names.length; i++) {
  console.log(`Index ${i}: ${names[i]}`);
}

// 3. შექმენით პროგრამა, რომელიც მასივში თითოეულ რიცხვს ამრავლებს 2-ზე და შედეგს ბეჭდავს მათ for ციკლის გამოყენებით.
const numbersToDouble = [2, 4, 6, 8];

for (let i = 0; i < numbersToDouble.length; i++) {
  console.log(numbersToDouble[i] * 2);
}

// 4. დაწერეთ ფუნქცია, რომელიც for ციკლის გამოყენებით ითვლის მასივში რამდენი ელემენტია 10-ზე მეტი.
function countGreaterThanTen(array) {
  let count = 0;
  for (let i = 0; i < array.length; i++) {
    if (array[i] > 10) {
      count++;
    }
  }
  return count;
}

// მაგალითი
const sampleNumbers = [5, 12, 8, 20, 15];
console.log(countGreaterThanTen(sampleNumbers)); // Output: 3

// 5. გამოიყენეთ for ციკლი მასივის ყველა ელემენტის შესაჯამებლად და საბოლოო შედეგის დასაბეჭდად.
const numbersToSum = [1, 2, 3, 4, 5];
let sum = 0;

for (let i = 0; i < numbersToSum.length; i++) {
  sum += numbersToSum[i];
}

console.log("Sum:", sum); // Output: 15
