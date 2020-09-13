// Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
// Note: For the purpose of this problem, we define empty string as valid palindrome.

// Input: "A man, a plan, a canal: Panama"
// Output: true
// Input: "race a car"
// Output: false

var isPalindrome = function(s) {
  // edge case
  if (s === "") return true
  // toLowerCase() does not mutate
  let lc = s.toLowerCase()
  // filter regex for letters & numbers, turn into array
  let lettersArray = lc.split('').filter(char => /[0-9A-Za-z]/.test(char));
  // .slice to copy array, because .reverse() mutates original array
  let reverseArray = lettersArray.slice().reverse()
  // if array = array.reverse, return true, else return false
  return lettersArray.every((val, index) => val === reverseArray[index]);
};