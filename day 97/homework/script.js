const result = document.getElementById("result")

// ეკრანზე ტექსტის დამატება
const display = (btnValue) => {
    result.value += btnValue
}

// ეკრანის გასუფთავება
const clearDisplay = () => {
    result.value = ""
}

// ჩვეულებრივი გამოთვლა
const calculate = () => {
    try {
        result.value = eval(result.value)
    } catch {
        result.value = "Error"
    }
}

const evenOdd = () => {

    const numberMatch = result.value.match(/-?\d+\.?\d*/)

    if(!numberMatch){
        result.value = "No numbers found!"
        return
    }

    const number = Number(numberMatch[0])

    if(number % 2 === 0){
        result.value = "Even"
    } else {
        result.value = "Odd"
    }
}

/*
    power():
     ინფუთში რასაც წაიკითხავს (რიცხვს)
     გამოთქვამს base ** exponent
*/
const power = () => {

    const baseMatch = result.value.match(/-?\d+\.?\d*/)

    if(!baseMatch){
        result.value = "Enter number first!"
        return
    }

    const base = Number(baseMatch[0])
    const exp = Number(prompt("რამდენ ხარისხში ავიყვანო?"))

    if(isNaN(exp)){
        result.value = "Invalid exponent"
        return
    }

    result.value = base ** exp
}
