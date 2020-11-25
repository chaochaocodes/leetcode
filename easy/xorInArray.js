// Given an integer n and an integer start.
// Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
// Return the bitwise XOR of all elements of nums. 

// Example 1:
// Input: n = 5, start = 0
// Output: 8
// Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
// Where "^" corresponds to bitwise XOR operator.


// Time Complexity: O(N), where N = size of array
// SOLUTION #1
var xorOperation = function(n, start) {
  // variable to store XOR of the array as a result
  let xor = 0
  // iterate through array and find XOR using '^' operator
  for (let i = 0; i < n; i++) {
      xor ^= start + 2*i
  }
  // result variable stores the XOR of all elements in the array
  return xor
};

// SOLUTION #2
const xorOperation = (n, start) => {
  let numsArray = [];
  let result;
  
  for (let i = 0; i < n; i++) {
      numsArray.push(start + 2 * i);
  }
  
  for (let i = 0; i < numsArray.length; i++) {
      result ^= numsArray[i];
  }
  
  return result;
}