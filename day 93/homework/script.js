const form = document.getElementById('signup-form');
const emailInput = document.getElementById('email');
const errorMessage = document.querySelector('.error-message');
const successSection = document.querySelector('.success-section');
const formSection = document.querySelector('.form-section');
const userEmailSpan = document.getElementById('user-email');
const dismissBtn = document.getElementById('dismiss-btn');

form.addEventListener('submit', function(e) {
  e.preventDefault();
  const emailValue = emailInput.value.trim();

  if (!validateEmail(emailValue)) {
    errorMessage.style.display = 'block';
    emailInput.style.borderColor = 'red';
  } else {
    errorMessage.style.display = 'none';
    emailInput.style.borderColor = 'hsl(0, 0%, 80%)';
    userEmailSpan.textContent = emailValue;
    formSection.classList.add('hidden');
    successSection.classList.remove('hidden');
  }
});

dismissBtn.addEventListener('click', () => {
  successSection.classList.add('hidden');
  formSection.classList.remove('hidden');
  emailInput.value = '';
});

function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}
