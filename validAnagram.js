// Given two strings s and t , write a function to determine if t is an anagram of s.
// Note: You may assume the string contains only lowercase alphabets.
// Follow up:  What if the inputs contain unicode characters? How would you adapt your solution to such case?

// Input: s = "anagram", t = "nagaram" // true
// Input: s = "rat", t = "car"  // false

var isAnagram = function(s, t) {
  if (s.length !== t.length) return false
  if (s == "" && t == "") return true
  let sSort = s.split('').sort()
  let tSort = t.split('').sort()

  let j = 0
    for (i = 0; i < sSort.length; i++) {
      if (sSort[i] === tSort[j] && sSort.length === 1) { return true }
      if (sSort[i] !== tSort[j]) { return false }
      else if (sSort[i] === tSort[j]) {
        j++
      }
    }
    return true
};

