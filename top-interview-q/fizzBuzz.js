/** LeetCode
 * @param {number} n
 * @return {string[]}
 */
// Write a program that outputs the string representation of numbers from 1 to n.
// But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. 
// For numbers which are multiples of both three and five output “FizzBuzz”.
// n = 5,
// Return:
// [
//     "1",
//     "2",
//     "Fizz",
//     "4",
//     "Buzz",
// ]

var fizzBuzz = function(n) {
  let i = 1
  let result = []
  while (i < n+1) {
      if (i % 3 === 0 && i % 5 === 0) result.push('FizzBuzz')
      else if (i % 3 === 0) result.push('Fizz')
      else if (i % 5 === 0) result.push('Buzz')
      else result.push(i.toString())
      i++
  }
  return result
};



// Hackerrank, return as strings on new line
var fizzBuzz = function(n) {
  let i = 1
  // let result = []
  while (i < n+1) {
      if (i % 3 === 0 && i % 5 === 0) console.log('FizzBuzz')
      else if (i % 3 === 0) console.log('Fizz')
      else if (i % 5 === 0) console.log('Buzz')
      else console.log(i.toString())
      i++
  }
  // return result
};

// n = 15,
// Return:
//  1
//  2
//  Fizz
//  4
//  Buzz