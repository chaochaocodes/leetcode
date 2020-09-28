// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
/**
 * @param {string} s
 * @return {boolean}
 */
// var isValid = function(s) {
//     stack = []
//     for (i = 0; i < s.length; i++){
//     open = stack[stack.length-1]
//         if (s[i] == "(" || s[i] == "[" || s[i] == "{") {
//           stack.push(s[i])
//         }
//         else if ((s[i] == ")" && open == "(") || (s[i] == "]" && open == "[" ) || (s[i] == "}" && open == "{")) {
//             stack.pop()
//         } else return false
//     } 
//     return (stack.length ? false : true)
// };

// Runtime: 64 ms, faster than 35.47% of JavaScript online submissions for Valid Parentheses.
// Memory Usage: 37.4 MB, less than 6.67% of JavaScript online submissions for Valid Parentheses.


isValid = s =>  {
  let map = {
      ")": "(",
      "}": "{",
      "]": "["
  }
  let stck = [];
  for(let i = 0; i < s.length; i ++){
      if(s[i] === "(" || s[i] === "[" || s[i] === "{") {
          stck.push(s[i]);
      } else if (stck[stck.length -1] === map[s[i]]) { 
          stck.pop()
      } else return false;
  }
  return stck.length ? false : true
}