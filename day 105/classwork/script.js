const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(item => {
  const btn = item.querySelector('.toggle');
  item.querySelector('.faq-question').addEventListener('click', () => {
    


    // ამ კონკრეტულის გახსნა/დახურვა
    item.classList.toggle('active');
    btn.textContent = item.classList.contains('active') ? "-" : "+";
  });
});