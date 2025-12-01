// მოთხოვნის გაგზავნა მითითებულ საიტზე
fetch('https://fakestoreapi.com/products/1')
  .then(response => response.json()) // პასუხის გარდაქმნა JSON ფორმატში
  .then(gabo => {
    // გამოტანა მთელი JSON ობიექტის
    console.log("მთლიანი JSON ობიექტი:", data);

    // კონკრეტული კუთვნილებების გამოტანა
    console.log("ID:", gabo.id);
    console.log("სათაური (title):", gabo.title);
    console.log("ფასი (price):", gabo.price);
    console.log("აღწერა (description):", gabo.description);
    console.log("კატეგორია (category):", gabo.category);
  })
  .catch(error => {
    console.error("შეცდომა:", error);
  });