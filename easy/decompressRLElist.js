// We are given a list nums of integers representing a list compressed with run-length encoding.
// Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.
// Return the decompressed list.

// Example 1:
// Input: nums = [1,2,3,4]
// Output: [2,4,4,4]
// Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
// The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
// At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

/**
 * @param {number[]} nums
 * @return {number[]}
 */

// SOLUTION #1
var decompressRLElist = function(nums) {
  // loop through pairs: [nums[2*i], nums[2*i+1]]
  // i=0, freq/val: nums[0], nums[1] 
  // i=1, freq/val: nums[2], nums[3]
  
  // freq/val: 1, 2 => generate [2]
  // freq/val: 3, 4 => generate [4,4,4]
  // let temp = new Array(3).fill(4)
  
  let result = []
  let n = nums.length/2
  for (let i=0; i<n; i++){
      let sublist = new Array(nums[2*i]).fill(nums[2*i+1])
      result = result.concat(sublist)
  }
  return result 
};

// SOLUTION #2
// loop through pairs with i+=2, 'concat' with spread operator
var decompressRLElist = function(nums) {
  let length = nums.length;
  let result = [];
  for(let i = 0; i < length; i += 2) {
      result.push(...new Array(nums[i]).fill(nums[i + 1]));
  };
  return result;
};