// Given a 32-bit signed integer, reverse digits of an integer.
// Note: Assume we are dealing with an environment which could only store 
// integers within the 32-bit signed integer range: [−231,  231 − 1]. 
// Assume that your function returns 0 when the reversed integer overflows.

var reverse = function(x) {
  const max = Math.pow(2,31) - 1
  const min = Math.pow(-2,31)
  const res = x.toString().split("").reverse().join("");

  // string to integer, take into account negative integers
  const sign = parseInt(res) * Math.sign(x)
  return sign > min && sign < max ? sign : 0
};