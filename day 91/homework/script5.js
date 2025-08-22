// 1) ღილაკზე დაკლიკება
document.getElementById("btn1").addEventListener("click", function(event) {
    console.log("ღილაკზე დაკლიკდა");
    console.log("Event target:", event.target); // რომელი ელემენტი დააკლიკეს
});

// 2) ტექსტის ველში კლავიატურის დაჭერა
document.getElementById("textInput").addEventListener("keydown", function(event) {
    console.log("დაჭერილია ღილაკი:", event.key);
});

// 3) მაუსის გადატარება div-ზე
document.getElementById("hoverBox").addEventListener("mouseover", function(event) {
    console.log("მაუსი შევიდა ელემენტზე:", event.target.id);
});

// 4) ფორმის გაგზავნის ბლოკვა
document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); // ბლოკავს ფორმის გაგზავნას
    console.log("ფორმა არ გაიგზავნა");
});

// 5) მაუსის კოორდინატების გამოტანა
document.addEventListener("mousemove", function(event) {
    console.log(`მაუსის პოზიცია: X=${event.clientX}, Y=${event.clientY}`);
});