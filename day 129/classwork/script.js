const emojis = [
  "😀",
  "😎",
  "🚀",
  "🌈",
  "🍕",
  "🐶",
  "🐱",
  "🌲",
  "🔥",
  "⚽",
  "💡",
  "🎉",
  "🤔",
  "👍",
  "😭",
  "💻",
  "🎨",
  "🧠",
  "😍",
  "😂"
];

document.getElementById("btn").addEventListener("click", function() {
  const randomIndex = Math.floor(Math.random() * emojis.length);
  console.log(emojis[randomIndex]);
  document.getElementById("output").textContent = emojis[randomIndex];
});




