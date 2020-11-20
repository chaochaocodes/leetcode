// A string is a valid parentheses string (denoted VPS) if it meets one of the following:

// It is an empty string "", or a single character not equal to "(" or ")",
// It can be written as AB (A concatenated with B), where A and B are VPS's, or
// It can be written as (A), where A is a VPS.

// For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

var maxDepth = function(s) {
  let count = 0
  let maxCount = 0
  for (let i=0; i<s.length; i++) {
      if (s[i] == "(") {
          count++
          maxCount = Math.max(maxCount, count)
      } else if (s[i] == ")") {
          count--
      }   
  }
  return maxCount
};
