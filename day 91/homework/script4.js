// მოვლენის მსმენელი: click + Enter/Space კლავიატურაზე
const box = document.getElementById("lemonBox");

/*
 addEventListener("click", fn) — ისმენს მაუსის დაკლიკებას ელემენტზე.
 ამ შემთხვევაში ვურთავთ/ვხსნით .lemon კლასს, რომელიც ცვლის border-radius-ს
 და დივი იღებს "ლიმონის" ფორმას.
*/
box.addEventListener("click", () => {
  box.classList.toggle("lemon");
});

// კლავიატურით same ქცევა (წვდომადობა)
box.addEventListener("keydown", (event) => {
  const key = event.key.toLowerCase();
  if (key === "enter" || key === " ") {
    event.preventDefault();
    box.classList.toggle("lemon");
  }
});
