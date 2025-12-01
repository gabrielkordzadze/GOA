// 1) კომენტარის სახით ახსენით რა არის localstorage და დაწვრილებით ჩამოაყალიბეთ იგი თქვენივე სიტყვებთ 

// localStorage — ეს არის ბრაუზერის მიერ შემოთავაზებული ვებ-შენახვის (web storage) ინტერფეისი, რომელიც საშუალებას გვაძლევს
// შევინახოთ ადგილობრივი მონაცემები (key/value წყვილები) მომხმარებლის ბრაუზერში. ეს მონაცემები ინარჩუნებენ თავს 
// მაშინაც კი, თუ გვერდი გადატვირთულია ან ბრაუზერი დაიხურა და თავიდან გაიხსნება — დამოუკიდებლად სესიიდან.
//
// localStorage-ის მონაცემები არ იწმინდება ავტომატურად ბრაუზერის დახურვისას (თვითონ რომ იყოს “session” ტიპის), 
// იგი ინარჩუნებს მონაცემებს მანამდე, სანამ არ წაიშლება explícitamente (პროგრამულად ან მომხმარებლის მანით).
//
// `localStorage` ან `sessionStorage` ორივე ეკუთვნის Web Storage API-ს — ეს არის უფრო თანამედროვე, შუშხუნა “cookie”-ების ალტერნატივა, 
// თუმცა ისინი განსხვავებულ მდგომაროებებს ჰყოფენ (expire time, შუალედი და ა.შ.).

// 2) ჩამოწერეთ დღეს ნასწავლი ყველა მეთოდი რომელიც უკავშირდება localstorage'ს ახსენით კომენტარის სახით და გააკეთეთ
// მაგალითებიც 

// 1) setItem — ქმნის ახალ ან ამახინჯებს არსებულ ჩანაწერს
localStorage.setItem("username", "ana");
// თუ “username” უკვე არსებობს, გადაფარავს და დააყენებს ახალ მნიშვნელობას

// 2) getItem — იღებს მნიშვნელობას ბრძანებით key-ით
let name = localStorage.getItem("username");
console.log(name); // "ana" თუ ადრე შეინიშნა; თუ ასეთი key არ არსებობს — null დაბრუნდება

// 3) removeItem — წაშლის კონკრეტულ key-ს ჰარმონიული მონაცემები
localStorage.removeItem("username");
// ახლა getItem(“username”) გამოგვাবে null-ს

// 4) clear — წაშლის **ყველა** ჩანაწერს localStorage-ში
localStorage.clear();
// ყველა არსებული key-value წყვილი გაქრება

// 5) key — ფუნქცია, რომელიც ავტომატურად ბრუნებს key-ს მისამართით index-ით
// მაგ: თუ შენ გაქვს რამდენიმე ჩანაწერი და გინდა ვიცოდე პირველი key:
let firstKey = localStorage.key(0);
console.log(firstKey); // შესაძლო “someKey” (პირველი ინსტანციის მიხედვით)

// 6) length — აღნიშნავს, რამდენი key-value წყვილი ინახება დამხმარე localStorage-ში
let count = localStorage.length;
console.log(count); // მაგალითად, 2 თუ ორი ჩანაწერი გვაქვს


// 3) კომენტარის სახით ჩამოაყალიბეთ რატომ ინახება ჩვენს მიერ შენახული ინფორმაცია string'ის სახით localstorage'ში 
// localStorage მხოლოდ string ტიპის მონაცემებს (Plain text) ინახავს, არ შეუძლია პირდაპირ სხვა ტიპები 
// (მაგალითად, ობიექტები, მასივები, ბულინი, ნెంబერი) — ისინი აუცილებელია გადაიყვანო string ფორმატში, 
// ჩვეულებრივ JSON.stringfy / JSON.parse მეთოდებით.
//
// ტექნიკური მიზეზი არის იგივე, რაც სხვა many storage apis-ში — რაც ნაკლებად რთული და სტაბილური წასაკრავი ფორმატით გადატანა. 
// თუ შენ ჩაწერ (setItem) ნიშანი, JavaScript ავტომატურად შეაკეთებს `.toString()` ან ისინი უნდა მიაწოდო უკვე string-ად.
//
// ამიტომ მოგიწევს:
// localStorage.setItem("user", JSON.stringify({ name: "ana", age: 25 }));
// და შემდეგ მისაღებად:
// let obj = JSON.parse(localStorage.getItem("user"));
// // ახლა obj არის { name: "ana", age: 25 } ობიექტი





// Find the smallest integer in the array
function findSmallestInt(arr) {
  // spread ოპერატორით გადავალთ მასივის ელემენტებს Math.min-ში
  return Math.min(...arr);
}


// Grasshopper - Summation
var summation = function (num) {
  let total = 0;
  for (let i = 1; i <= num; i++) {
    total += i;
  }
  return total;
};


//Counting sheep...
function countSheeps(sheep) {
  let count = 0;
  for (let i = 0; i < sheep.length; i++) {
    if (sheep[i] === true) {
      count++;
    }
  }
  return count;
}


//You Can't Code Under Pressure #1
function doubleInteger(i) {
  // i will be an integer. Double it and return it.
  return i * 2;
}


//Returning Strings
function greet(name){
  //your code here
  return `Hello, ${name} how are you doing today?`;
}


//Keep Hydrated!
function litres(time) {
  return Math.floor(time * 0.5);
}

//Beginner - Lost Without a Map
function maps(x){
    return x.map(n => n * 2);

}