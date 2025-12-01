// Array plus array
function arrayPlusArray(arr1, arr2) {
  let sum = 0;

  for (let num of arr1) {
    sum += num;
  }

  for (let num of arr2) {
    sum += num;
  }

  return sum;
}


// Convert a string to an array
function stringToArray(string){
  return string.split(" ");
}


// Convert number to reversed array of digits
function digitize(n) {
  //code here
  return String(n).split('').reverse().map(Number);      
}


// Remove String Spaces
function noSpace(x){
  let result = "";
  for (let i = 0; i < x.length; i++) {
    if (x[i] !== " ") {   
      result += x[i];  
    }
  }
  return result;
}


// Find the smallest integer in the array
function findSmallestInt(arr) {
  // spread ოპერატორით გადავალთ მასივის ელემენტებს Math.min-ში
  return Math.min(...arr);
}


// Remove First and Last Character
function removeChar(str){
  // slice(1, -1) — ვიწყებთ 1-ის ინდექსიდან და ვასრულებთ ბოლო ინდექსის წინ
  return str.slice(1, -1);
}


// Sum of positive
function positiveSum(arr) {
  let sum = 0; 


  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      sum += arr[i];
    }
  }

  return sum;
}


// Convert a Number to a String!
function numberToString(num) {
  return num.toString()
  
}


// Merge two sorted arrays into one
function mergeArrays(arr1, arr2) {
  let merged = [...arr1, ...arr2];

  merged.sort((a, b) => a - b);

  let final = [];
  for (let num of merged) {
    if (!final.includes(num)) {
      final.push(num);
    }
  }

  return final;
}
