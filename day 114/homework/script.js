// პუნქტი: ვიღებთ პროდუქტების მონაცემებს Fake Store API-დან
fetch('https://fakestoreapi.com/products')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('products-container');

    // თითოეული პროდუქტის მონაცემის გამოყენება
    data.forEach(product => {
      // div შექმნა პროდუქტისთვის
      const productDiv = document.createElement('div');
      productDiv.classList.add('product');

      // პროდუქტის ფოტო
      const img = document.createElement('img');
      img.src = product.image;
      productDiv.appendChild(img);

      // პროდუქტის სახელი
      const title = document.createElement('h2');
      title.textContent = product.title;
      productDiv.appendChild(title);

      // პროდუქტის ფასი
      const price = document.createElement('p');
      price.textContent = `$${product.price}`;
      productDiv.appendChild(price);

      // div დამატება container-ში
      container.appendChild(productDiv);
    });
  })
  .catch(error => console.log('Error fetching products:', error));
