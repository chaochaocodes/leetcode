function longestCommonPrefix(strs) {
  if (strs.length === 0) return '';
  // loop through no more than length of first string
  for (let i = 0; i < strs[0].length; i++) {
    // for ... of loop 
    for (let str of strs) {
      // compare first letter of each string against first string's first letter
      if (str[i] !== strs[0][i]) {
        // slice to return common letters
        return str.slice(0, i);
      }
    }
  }
  return strs[0];
}

// let input = ["flower","flow","flight"]
// Output: "fl"