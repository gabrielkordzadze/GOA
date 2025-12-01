// 1) დაბეჭდეთ for loops-ის დახმარებით კენტრი რიცხვები 1-დან 76-მდე/
for (let i = 1; i <= 76; i++) {
  if (i % 2 !== 0) {
    console.log(i);
  }
}

// 2) შექმენით ობიექტი, რომელშიც შეინახავთ თქვენთვის სასურველ key და value-ებს. თქვენი დავალებაა for in iterator-ის დახმარებით დაბეჭდოთ ობიექტში მყოფი ყველა key და value.
const myObject = {
  name: "Gabriel",
  age: 22,
  city: "Tbilisi",
  hobby: "coding"
};

for (let key in myObject) {
  console.log(key + ": " + myObject[key]);
}

// 3) შექმენით 6 ელემენტიანი სია, თქვენი დავალებაა დაბეჭდოთ ამ სიაში მყოფი ყველა ელემენტი for of iterator-ის დახმარებით.
const myList = ["apple", "banana", "cherry", "date", "fig", "grape"];

for (let item of myList) {
  console.log(item);
}

// 4) კომენტარების სახით თქვენი სიტყვებით ახსენით რა არის localStorage და მისი მეთოდები.

// localStorage არის ბრაუზერში არსებული შეზღუდული ტიპის მონაცემთა საცავი, რომელიც საშუალებას აძლევს
// ჩვენ შევინახოთ key-value წყვილები და ინფორმაცია დარჩეს ბრაუზერის დახურვის შემდეგაც.

// მთავარი მეთოდები:
// - .setItem(key, value) - მნიშვნელობის შენახვა.
// - .getItem(key) - მნიშვნელობის წაკითხვა.
// - .removeItem(key) - კონკრეტული key-ის წაშლა.
// - .clear() - ყველა შენახული მონაცემის წაშლა.
// - .length - localStorage-ში არსებული ელემენტების რაოდენობა.
// - .key(index) - index-ის მიხედვით key-ის მიღება.


// 5) localStorage-სა და .setItem() ფუნქციის დახმარებით შეინახეთ 7 მნიშვნელობა storage-ში თქვენთვის სასურველი key და value-ები.
localStorage.setItem("name", "Gabriel");
localStorage.setItem("age", "22");
localStorage.setItem("city", "Tbilisi");
localStorage.setItem("hobby", "coding");
localStorage.setItem("language", "JavaScript");
localStorage.setItem("food", "pizza");
localStorage.setItem("drink", "coffee");

// 6) წინა დავალებაში გაკეთებულ localStorage-ში შენახული მნიშვნელობებიდან ამოშალეთ .removeItem() ფუნქციის დახმარებით ნებისმიერი 2 მნიშვნელობა.
localStorage.removeItem("food");
localStorage.removeItem("drink");

// 7) დაბეჭდეთ და console-ში გამოიტანეთ თქვენი localStorage-ი სიგრძე .length მეთოდის დახმარებით.
console.log(localStorage.length); // 5

// 8) localStorage-დან წამოიღეთ .getItem()-ის დახმარებით მნიშვნელობები და შეინახეთ შესაბამისს ცვლადებში. ბოლოს დაბეჭდეთ ყველა ცვლადის შიგთავსი ;>
const name = localStorage.getItem("name");
const age = localStorage.getItem("age");
const city = localStorage.getItem("city");
const hobby = localStorage.getItem("hobby");
const language = localStorage.getItem("language");

console.log(name, age, city, hobby, language);

// 9) .clear() ფუნქციის დახმარებით გაასუფთავეთ თქვენი localStorage()
localStorage.clear();

// 10) შეინახეთ კვლავ 2 ახალი მნიშვნელობა localStorage-ში და დაბეჭდეთ მათი key-ები index-ების მეშვეობით .key() ფუნქციის დახმარებით.
localStorage.setItem("fruit", "apple");
localStorage.setItem("drink", "tea");

console.log(localStorage.key(0)); // fruit
console.log(localStorage.key(1)); // drink