// No zeros for heroes
function noBoringZeros(n) {
  // your code
  if (n === 0) 
    return 0;           

  while (n % 10 === 0) {          
    n = n / 10;                   
  }

  return n;
}


// Keep Hydrated!
function litres(time) {
  return Math.floor(time * 0.5);
}


// Count the Monkeys!
function monkeyCount(n) {
// your code here
  let arr = [];
  
  for (let i = 1; i <= n; i++) {
    arr.push(i);
  }
  
  return arr;
}


// Surface Area and Volume of a Box
function getSize(width, height, depth) {
  const surfaceArea = 2 * (width * height + width * depth + height * depth);
  const volume = width * height * depth;
  
  return [surfaceArea, volume];
}