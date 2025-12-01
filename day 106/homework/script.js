// Function 1 - hello world
function greet(){
  return "hello world!"
}


// Counting sheep...
function countSheeps(sheep) {
  let count = 0;
  for (let i = 0; i < sheep.length; i++) {
    if (sheep[i] === true) {
      count++;
    }
  }
  return count;
}


// Basic Mathematical Operations
function basicOp(operation, value1, value2){
  if (operation === '+') {
    return value1 + value2;
  } else if (operation === '-') {
    return value1 - value2;
  } else if (operation === '*') {
    return value1 * value2;
  } else if (operation === '/') {
    return value1 / value2;
  } else {
    return null; // invalid operator
  }
}


// Century From Year
function century(year) {
  return Math.floor((year - 1) / 100) + 1;
}


// Sum Arrays
function sum (numbers) {
  let total = 0;            
  for (let i = 0; i < numbers.length; i++) {
    total += numbers[i];    
  }
  return total;             
}


// Are You Playing Banjo?
function areYouPlayingBanjo(name) {
  // Implement me
  if (name[0] === 'R' || name[0] === 'r') {
    return name + " plays banjo";
  } else {
    return name + " does not play banjo";
  }
}