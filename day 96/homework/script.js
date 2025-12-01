// ვპოულობთ იმ ელემენტს, სადაც შედეგი უნდა გამოჩნდეს (input ველი)
const result = document.getElementById("result")

// ეს ფუნქცია ამატებს ღილაკზე დაწერილ სიმბოლოს ეკრანზე
const display = (btnValue) => {
    // result.value არის ის, რაც ეკრანზეა, მაგას ვუმატებთ ღილაკის მნიშვნელობას
    result.value += btnValue
}

// ეს ფუნქცია ასუფთავებს ეკრანს ("C" ღილაკისთვის)
const clearDisplay = () => {
    // უბრალოდ ვწერთ ცარიელ სტრიქონს
    result.value = ""
}

// ეს ფუნქცია ითვლის შედეგს ("=" ღილაკისთვის)
const calculate = () => {
    // eval() ფუნქცია კითხულობს ტექსტს და ასრულებს როგორც მათემატიკურ გამოთვლას
    // მაგალითად თუ input-ში წერია "2+3*4", eval ამას გადააქცევს 14-ად
    result.value = eval(result.value)
}

// ეს ფუნქცია ამოწმებს, ეკრანზე არსებული რიცხვი ლუწია თუ კენტი
const evenOdd = () => {
    // ეს სიმბოლოები არიან ნებადართული რიცხვებისთვის
    const validSymbols = ["0","1","2","3","4","5","6","7","8","9"]

    // finalNumber აქ შეინახება მხოლოდ ციფრები
    let finalNumber = ""

    // ვატარებთ ციკლს input-ში არსებულ თითოეულ სიმბოლოზე
    for (let i = 0; i < result.value.length; i++) {
        // ვამოწმებთ, სიმბოლო რიცხვია თუ არა
        if (result.value[i] in validSymbols) {
            // თუ რიცხვია, ვამატებთ finalNumber-ში
            finalNumber += result.value[i]
        }
    }

    // ვამოწმებთ, finalNumber ლუწია თუ კენტი
    if (finalNumber % 2 == 0) {
        result.value = "Even" // თუ ლუწია, ეკრანზე გამოიტანს Even
    } else {
        result.value = "Odd" // თუ კენტია, ეკრანზე გამოიტანს Odd
    }
}