// 1
const removeBtn = document.getElementById("removeBtn");
removeBtn.addEventListener("click", () => {
  const box1 = document.getElementById("box1");
  const btn = document.getElementById("btn-inside-1");

  if (btn) {
    btn.remove();

    const msg = document.createElement("span");
    msg.textContent = " (ღილაკი ამოშლილია)";
    msg.className = "muted";
    box1.appendChild(msg);

    removeBtn.disabled = true;
  }
});

// 2
const replaceBtn = document.getElementById("replaceBtn");
replaceBtn.addEventListener("click", () => {
  const box2 = document.getElementById("box2");
  const oldButton = document.getElementById("btn-inside-2");
  const paragraph = document.getElementById("paragraph-to-move");

  if (oldButton && paragraph) {
    box2.replaceChild(paragraph, oldButton);
    replaceBtn.disabled = true;
  }
});
