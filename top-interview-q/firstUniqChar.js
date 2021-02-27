// Given a string, find the first non-repeating character in it and return its index. 
// If it doesn't exist, return -1.
// Note: You may assume the string contains only lowercase English letters.

// s = "leetcode" // return 0.
// s = "loveleetcode" // return 2.

var firstUniqChar = function(s) {
  for(i=0;i<s.length;i++){
      // if first and last encounter of the letter is the same, it must be unique
      if (s.indexOf(s[i])===s.lastIndexOf(s[i])){
         return i;
     } 
  }
  return -1;
};