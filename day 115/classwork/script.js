// API-ში მოთხოვნა
fetch('https://fakestoreapi.com/products/1')
  .then(response => response.json())
  .then(data => {
    // HTML-ში ინფორმაციის დამატება
    const productDiv = document.getElementById('product');
    productDiv.innerHTML = `
      <img src="${data.image}" alt="${data.title}">
      <h2>${data.title}</h2>
      <p><strong>ფასი:</strong> $${data.price}</p>
      <p>${data.description}</p>
      <p><strong>კატეგორია:</strong> ${data.category}</p>
    `;
  })
  .catch(error => console.error('შეცდომა:', error));