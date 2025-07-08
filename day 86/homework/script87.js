// 1)შექმენით სია 30 ელემენტით, შემდგომ გადაურეთ მას ფორ ლუპით,  და გამოიტანეთ ყველა ელემნტი
// გამოიყენეთ of 
let myList = [];

for (let i = 0; i < 30; i++) {
  myList[i] = i + 1;
}

for (let item of myList) {
  console.log(item);
}


// 2)შექმენით 2 სია, შემდეგ პირველ სიაში ჩაამატეთ 10 ელემენტი,შემდეგ პირველი სიიდან მეორე სიაში ჩამატეთ ყველა ელემნტი ფორ ლუპით
// გამოიყენთ of
let list1 = [];

for (let i = 0; i < 10; i++) {
  list1[i] = i + 1;
}

let list2 = [];

for (let i = 0; i < list1.length; i++) {
  list2[i] = list1[i];
}

console.log("List1:", list1);
console.log("List2:", list2);


// 3)სტრინგს გადაუარეთ ფორ ლუპით და შეამოწმე არის თუარა ის ხმოვანი, თუ არის გამოიტანეთ თუარა არ გამოიტანოთ
// გამოიენეთ of
let text = "Hello World";

for (let char of text.toLowerCase()) {
  if (
    char === 'a' ||
    char === 'e' ||
    char === 'i' ||
    char === 'o' ||
    char === 'u'
  ) {
    console.log(char);
  }
}


// 4)ახსენით რა არის block scope, global scope, local scope

// Global Scope – ცვლადი გამოცხადებულია სკრიპტის გარეთ ან პირდაპირ გლობალურ სივრცეში. ყველგან გამოიყენება.

// Local Scope – ცვლადი გამოცხადებულია ფუნქციის შიგნით და მხოლოდ იქ მუშაობს.

// Block Scope – ცვლადი გამოცხადებულია ბლოკში ({}), მაგალითად if, for, while-ში let ან const-ით.

// 5)მოიყვანეთ მაგალითები block scope, global scope, local scope ზე

// Global Scope

let globalVar = "I'm global";

function showGlobal() {
  console.log(globalVar);
}

showGlobal(); // გამოიტანს: I'm global



// Local Scope

function myFunction() {
  let localVar = "I'm local";
  console.log(localVar);
}

myFunction(); // მუშაობს
// console.log(localVar); // შეცდომა! localVar არ არსებობს გლობალურად



// Block Scope

if (true) {
  let blockVar = "I'm block scoped";
  console.log(blockVar);
}

// console.log(blockVar); // შეცდომა! blockVar არსებობს მხოლოდ ბლოკში