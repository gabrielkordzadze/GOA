// Find numbers which are divisible by given number
function divisibleBy(numbers, divisor){
  return numbers.filter(num => num % divisor === 0);

}


// Drink about
function peopleWithAgeDrink(old) {
    if (old < 14) {
    return "drink toddy";
  } else if (old < 18) {
    return "drink coke";
  } else if (old < 21) {
    return "drink beer";
  } else {
    return "drink whisky";
  }
};



// Volume of a Cuboid
class Kata {
  static getVolumeOfCuboid(length, width, height) {
    // your code here
    return length * width * height;
  }
}