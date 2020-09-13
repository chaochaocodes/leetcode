// var myAtoi = function(str) {
//   // edge case1: if str = "", return 0
//   if (str.length === 0) return 0
//   // first non-white space is not +/- or number, return 0
//   const letter = str.split('').filter( el => /[0-9a-zA-Z\-\+]/.test(el)).join('')
//   const res = str.split('').filter( el => /[0-9\-\+]/.test(el)).join('');
//   console.log(letter)
//   console.log(letter[0])

//   const min = Math.pow(-2,31)
//   const max = Math.pow(2,31) - 1
//   if (letter < min) return min
//   if (letter > max) return max

//   const checkMM = res > min && res < max ? res : 0
//   return  (( letter[0].toUpperCase() != letter[0].toLowerCase() ) === true) ? 0 : (checkMM)
// }

var myAtoi = function(str) {
  return Math.max(Math.min(parseInt(str) || 0, 2147483647), -2147483648)
}

Input1 = "   -42"  // -42
Input2 = "4193 with words" // 4193
Input3 = "words and 987" // 0
// Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.
Input4 = "-91283472332" // -2147483648
// Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−2^31) is returned.
// min = 2147483648 --> 2^31
// max = 2147483647 --> 2^31 -1
Input5 = "3147483647"
Input6 = "3.14159" // 3.  Didn't account for non-alphanumeric characters

myAtoi(Input6)
