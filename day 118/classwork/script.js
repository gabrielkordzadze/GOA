const key = "1fab308981764501b85c1a214ded4756"
const city = "Sudan";

fetch(`https://api.openweathermap.org/data/2.5/weather?q=
    ${encodeURIComponent(city)}&appid=${key}&units=metric`)
    .then(res => res.json())
    .then(data => {
        console.log("ამინდი:", data.weather[0].main);
        console.log("აღწერა:", data.weather[0].descripion);
        console.log("ტემპერატურა:", data.main.temp);
        console.log("ქარის სიჩქარე:", data.wind.speed);
    })
