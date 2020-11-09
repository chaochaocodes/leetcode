// Given a word, you need to judge whether the usage of capitals in it is right or not.

// We define the usage of capitals in a word to be right when one of the following cases holds:

// All letters in this word are capitals, like "USA".
// All letters in this word are not capitals, like "leetcode".
// Only the first letter in this word is capital, like "Google".
// Otherwise, we define that this word doesn't use capitals in a right way.
 
// Input: "FlaG"  // False

/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
  let caps = word.toLowerCase()
  
  if ((word.toUpperCase() === word) || (word.toLowerCase() === word)) {
      return true
  }
  else if ((caps[0].toUpperCase() + caps.substring(1)) === word) {
      return true
  }
  else return false
};