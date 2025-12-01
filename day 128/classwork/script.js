// Convert number to reversed array of digits
function digitize(n) {
  //code here
  return String(n).split('').reverse().map(Number);      
}


// Tip Calculator
function calculateTip(amount, rating) {
  const rate = rating.toLowerCase(); 

  if (rate === "terrible") {
    return 0;
  }
  if (rate === "poor") {
    return Math.ceil(amount * 0.05);
  }
  if (rate === "good") {
    return Math.ceil(amount * 0.10);
  }
  if (rate === "great") {
    return Math.ceil(amount * 0.15);
  }
  if (rate === "excellent") {
    return Math.ceil(amount * 0.20);
  }

  return "Rating not recognised";
}


// Find out whether the shape is a cube
function cubeChecker(volume, side){
  if (volume <= 0 || side <= 0) 
    return false
  return side ** 3 === volume;

};


// Beginner - Reduce but Grow
function grow(x){
  return x.reduce((product, num) => product * num, 1);
}