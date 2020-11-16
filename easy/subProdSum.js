// Input: n = 234
// Output: 15 
// Explanation: 
// Product of digits = 2 * 3 * 4 = 24 
// Sum of digits = 2 + 3 + 4 = 9 
// Result = 24 - 9 = 15

/**
 * @param {number} n
 * @return {number}
 */

// 1. brute force 
var subtractProductAndSum = function(n) {
  // convert integer to string, split and save in array
  let str = n.toString().split('')  // [2,3,4]

  let sum = 0
  let product = 1
  for (let i=0; i< str.length; i++) {
    sum += parseInt(str[i]) // convert back to integer, else js quirk sum = '0234'
    product *= str[i]
  }

  return product-sum
};


// 2.) Javascript: using toString().split('') to create the Array to reduce

var subtractProductAndSum = n => 
    n.toString().split('').map(Number).reduce((a, b) => a * b) -
    n.toString().split('').map(Number).reduce((a, b) => a + b);

// 3.) Javascript: using Array.from() to create the Array to reduce

var subtractProductAndSum = n =>
    Array.from(String(n), Number).reduce((a, b) => a * b) -
    Array.from(String(n), Number).reduce((a, b) => a + b);