/**
 * @param {number} n
 * @return {boolean}
 */
// Given an integer, write a function to determine if it is a power of three.
// 3^1 = 3, 3^2 = 9, 3^3 = 27, 3^4 = 81
// 1) will be divisible by 3 with remainder === 0
// 2) n keeps dividing until  n = 3, n /= 3 ==> n = 1
// Division assignment /= same as += ... 
// Operator: x /= y
// Meaning:  x  = x / y

var isPowerOfThree = function(n) {
  if (n < 1) return false
  
  while (n % 3 === 0 ) {
      n /= 3
  }
  return n == 1;
};
