const form = document.getElementById("myForm");
const result = document.getElementById("result");

// მასივი თვეების სახელებით
const months = [
    "იანვარი",
    "თებერვალი",
    "მარტი",
    "აპრილი",
    "მაისი",
    "ივნისი",
    "ივლისი",
    "აგვისტო",
    "სექტემბერი",
    "ოქტომბერი",
    "ნოემბერი",
    "დეკემბერი"
];

form.addEventListener("submit", function(e){
    e.preventDefault();

    const name = form.name.value.trim();
    const surname = form.surname.value.trim();
    let date = form.date.value; // yyyy-mm-dd

    if(!date) return; // თუ თარიღი არაა შეყვანილი

    const [year, month, day] = date.split("-");

    // თვე რიცხვით → თვის სახელად
    const monthName = months[parseInt(month, 10) - 1];

    result.innerHTML += `
        <p>Your Fullname is: ${name} ${surname}, You were born on ${day} ${monthName}, ${year}</p>
    `;
});