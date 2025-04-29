// ===== 3) მათემატიკური ოპერაციები (3-3 მაგალითი თითოეულზე) =====

console.log("მიმატება:");
console.log(2 + 3);
console.log(10 + 1);
console.log(-4 + 9);

console.log("გამოკლება:");
console.log(7 - 2);
console.log(10 - 10);
console.log(0 - 5);

console.log("გამრავლება:");
console.log(3 * 3);
console.log(5 * 0);
console.log(-2 * 4);

console.log("გაყოფა:");
console.log(8 / 2);
console.log(9 / 3);
console.log(10 / 4);

console.log("ნაშთი:");
console.log(7 % 2);
console.log(10 % 3);
console.log(6 % 2);

console.log("ხარისხში აყვანა:");
console.log(2 ** 3);
console.log(5 ** 2);
console.log(3 ** 0);

console.log("ერთით გაზრდა:");
let a = 5;
console.log(a++);
console.log(a);
let b = 10;
console.log(++b);

console.log("ერთით შემცირება:");
let c = 3;
console.log(c--);
console.log(c);
let d = 7;
console.log(--d);


// ===== 4) პარაგრაფის ტექსტის ამოღება და ცვლადში შენახვა =====

let ტექსტი = document.getElementById("myText").textContent;
console.log("პარაგრაფის ტექსტი:", ტექსტი);


// ===== 5) ცვლადის გაზრდა და გამოყვანა =====

let num = 5;
console.log("საწყისი:", num);  // საწყისი მნიშვნელობა: 5

// ზრდა 
console.log("ერთით გაზრდის შემდეგ:", num++);  // გამოიტანს: 5, თუმცა num გახდება 6

// ჯერ გაზრდა, შემდეგ გამოტანა
console.log("ჯერ გაზრდა, მერე გამოტანა:", ++num);  // გამოიტანს: 7 (რადგან უკვე გაზრდილია num)

