// 3 დავალება

// რეგისტრაციის ფორმის მოვლენის მსმენელი
document.getElementById("register-form").addEventListener("submit", function(e) {
    e.preventDefault(); // ბლოკავს ფორმის ავტომატურ გაგზავნას

    let name = document.getElementById("name").value.trim();

    // ინიციალების გამოთვლა
    let initials = name.split(" ").map(word => word[0].toUpperCase()).join("");
    console.log("მომხმარებლის ინიციალები:", initials);

    // რეგისტრაციის გვერდის დამალვა და მთავარი საიტის ჩვენება
    document.getElementById("register-page").style.display = "none";
    document.getElementById("main-site").style.display = "block";
});