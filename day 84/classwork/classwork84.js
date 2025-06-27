// 1) შექმენით ფუნქცია რომელსაც გადასცემთ მხოლოდ 1 პარამეტრს number'ს და for loop'ის მეშვეობით გამოიტანეთ ყველა რიცხვი შემოტანილი 
// number'ის ჩათვლით
function countToNumber(number) {
    let result = "";
    for (let i = 1; i <= number; i++) {
        result += i + " ";
    }
    return result.trim();
}

console.log(countToNumber(5)); 


// 2) შექმენით ფუნქცია რომელსაც გადასცემთ 2 პარამეტრს name და age შემდეგ შეამოწმეთ თუ შემოტანილი ასაკი ნაკლები იქნება 18 დააბრუნეთ 
// "your not adult yet" სხვა შემთხვევაში მიესალმეთ მომხმარებელს
function checkAge(name, age) {
    if (age < 18) {
        return "you are not adult yet";
    } else {
        return "Hello " + name + "!";
    }
}

console.log(checkAge("Gio", 17)); 
console.log(checkAge("Nino", 22)); 


// 3) შექმენით ფუნქცია რომელსაც გადაეცემა 1 პარამეტრი name შემდეგ for loop'ის საშუალებით გადაუარეთ ამ name'ის სიგრძეს და გამოიტანეთ თითოეული 
// ასო ამ სახელიდან
function printLetters(name) {
    let result = "";
    for (let i = 0; i < name.length; i++) {
        result += name[i] + " ";
    }
    return result.trim();
}

console.log(printLetters("Gio")); 
