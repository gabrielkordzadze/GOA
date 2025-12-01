//  Even or Odd
function evenOrOdd(number) {
  if(number % 2 === 0) {
    return "Even";
  } else{
    return "Odd";
  }
  
}



// Convert a Number to a String!
function numberToString(num) {
  return num.toString()
  
}



// Reversed Strings
function solution(str) {
  // ვაქცევთ სტრინგს მასივად
  // "world" -> ["w", "o", "r", "l", "d"]
  let arr = str.split('');

  // ვაბრუნებთ მასივს უკუღმა
  arr.reverse();

  // ვაერთიანებთ ისევ სტრინგად
  let reversed = arr.join('');

  // ვაბრუნებთ შედეგს
  return reversed;
}



// Return Negative
function makeNegative(num) {
  return -Math.abs(num);
}


// Convert boolean values to strings 'Yes' or 'No'.
function boolToWord( bool ){
  if(bool === true){
    return "Yes"
  }return "No"

}



// Sum of positive
function positiveSum(arr) {
  let sum = 0; // ვიწყებთ ჯამით 0

  // ვბრუნდებით მასივში თითო ელემენტზე
  for (let i = 0; i < arr.length; i++) {
    // თუ რიცხვი დადებითია, ვამატებთ ჯამში
    if (arr[i] > 0) {
      sum += arr[i];
    }
  }

  // საბოლოო ჯამს ვაბრუნებთ
  return sum;
}



// Remove First and Last Character
function removeChar(str){
  // slice(1, -1) — ვიწყებთ 1-ის ინდექსიდან და ვასრულებთ ბოლო ინდექსის წინ
  return str.slice(1, -1);
}



// Find the smallest integer in the array
function findSmallestInt(arr) {
  // spread ოპერატორით გადავალთ მასივის ელემენტებს Math.min-ში
  return Math.min(...arr);
}