// 1)შექმენით სია სადაც შეინახავთ მომხმარებლების ობიექტებს სადაც გექნებათ key/value (username email, city, age) შემდეგ გადაუარეთ ამ სიას 
// forEach-ის გამოყენებით და გამოიტანეთ საიტზე ყველა ელემენტი <p> / <b> / <div> თეგებში ლამაზად
// მომხმარებლების სია
const users = [
  { username: "gio", email: "gio@gmail.com", city: "Tbilisi", age: 20 },
  { username: "nino", email: "nino@gmail.com", city: "Kutaisi", age: 17 },
  { username: "dato", email: "dato@gmail.com", city: "Batumi", age: 25 },
  { username: "mari", email: "mari@gmail.com", city: "Rustavi", age: 16 }
];

const allUsersDiv = document.getElementById("all-users");
const adultUsersDiv = document.getElementById("adult-users");

// --- ყველა მომხმარებელი ---
users.forEach(user => {
  allUsersDiv.innerHTML += `
    <div style="margin-bottom:10px; border:1px solid #ccc; padding:8px;">
      <p><b>Username:</b> ${user.username}</p>
      <p><b>Email:</b> ${user.email}</p>
      <p><b>City:</b> ${user.city}</p>
      <p><b>Age:</b> ${user.age}</p>
    </div>
  `;
});

// 2)ზევით შექმნილი ობიექტი გაფილტრეთ ისე რომ საიტზე გამოიტანოთ მხოლოდ 18 წელზე მეტი ან ტოლი მომხმარებლები
const adults = users.filter(user => user.age >= 18);

adults.forEach(user => {
  adultUsersDiv.innerHTML += `
    <div style="margin-bottom:10px; border:1px solid green; padding:8px;">
      <p><b>Username:</b> ${user.username}</p>
      <p><b>Email:</b> ${user.email}</p>
      <p><b>City:</b> ${user.city}</p>
      <p><b>Age:</b> ${user.age}</p>
    </div>
  `;
});