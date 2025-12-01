// 1) for ციკლის დახმარებით დაბეჭდეთ ლუწი რიცხვები 1-დან 50-მდე.
for(let i = 1; i < 50; i++){
    if(i % 2 === 0)
        console.log(i)
}

// 2) შექმენით ობიექტი, რომელშიც key და იქნება სახელი, გვარი, ასაკი და value-ები შესაბამისი მნიშვნელობები. 
// თქვენი დავალებაა for in iterator-ის დახმარებით დაბეჭდოთ ობიექტში მყოფი key და value.
let person = {
    name: გაბრიელ,
    surname: კორძაძე,
    age: 14
} 

for(let key in person){
    console.log(key + ": " + person[key]);
}

// 3) შექმენით 6 ელემენტიანი რიცხვების სია, თქვენი დავალებაა for of iterator-ის დახმარებით დაბეჭდოთ სიაში მყოფი 
// მხოლოდ კენტი რიცხვები.
let numbers = [3, 8, 11, 20, 15, 6];

for (let num of numbers) {
  if (num % 2 !== 0) {
    console.log(num);
  }
}
