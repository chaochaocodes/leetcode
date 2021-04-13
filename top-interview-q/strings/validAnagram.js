// Given two strings s and t , write a function to determine if t is an anagram of s.
// Note: You may assume the string contains only lowercase alphabets.
// Follow up:  What if the inputs contain unicode characters? How would you adapt your solution to such case?

// Input: s = "anagram", t = "nagaram" // true
// Input: s = "rat", t = "car"  // false

// if input is a sentence, account for spaces and cases
// s = s.replace(/[^\w]/g, '').toLowerCase()

var isAnagram = function(s, t) {
  if (s.length !== t.length) return false
    
  let sSort = s.split('').sort().join('')
  let tSort = t.split('').sort().join('')
  
  return sSort === tSort
};