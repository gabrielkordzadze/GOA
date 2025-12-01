// 1) შეამოწმეთ, შეიცავს თუ არა სტრინგი 'programming' ქვესტრინგ 'ram'-ს
console.log("programming".includes("ram"))

// 2) შეამოწმეთ თუ სია[10, 20, 30] შეიცავს 20-ს.
console.log([10,20,30].includes(20))

// 3) იპოვეთ l-ის ინდექსი hello-ში
console.log("hello".indexOf("l"))

// 4) იპოვეთ 3-ის ინდექსი [1, 2, 3, 4]-ში.
console.log([1, 2, 3, 4].indexOf(3))

// 5) კონსოლში გამოიტანე პირველი სამი სიმბოლო 'JavaScript'-დან,
console.log("JavaScript".slice(0, 3))

// 6) კონსოლში გამოიტანე პირველი ორი ელემენტი [5, 6, 7, 8]-დან.
console.log([5, 6, 7, 8].slice(0, 2))

// 7) გაყავით apple-orange-banana სტრინგი --ზე და 1.2.3 სტრინგი ..-ზე.
let fruits = "apple-orange-banana".split("-")
console.log(fruits)


let numbers = "1.2.3".split(".")
console.log(numbers)

// 8) შეაერთეთ სია[cat, dog, bird] space-ბით 
let animals = ["cat", "dog", "bird"]
let result = animals.join(" ")
console.log(result);

// 9) შეაერთეთ სია [cat, dog, bird]  **-ით.
let animals1 = ["cat", "dog", "bird"]
let result1 = animals1.join("-")
console.log(result1);

// 10) დაალაგეთ სია [3, 1, 4, 1, 5] თანმიმდევრობით
let numbers1 = [3, 1, 4, 1, 5];
numbers1.sort()
console.log(numbers1); 

// 11) დაალაგეთ სია [ვაშლი, ჭიანჭველა, ზებრა] ანბანური თანმიმდევრობით.
let items = ["ვაშლი", "ჭიანჭველა", "ზებრა"]
items.sort()
console.log(items)
