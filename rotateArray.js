// Given an array, rotate the array to the right by k steps, where k is non-negative.

// Follow up:
// Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
// Could you do it in-place with O(1) extra space?

// Example:
// Input: nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]
// Explanation: 
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */

var rotate = function(nums, k) {
  if (nums.length <= 1 || k === 0) return nums
  
  
  let rotate = nums.splice(-k)
  
  while (k > 0) {
      nums.splice(0, 0, rotate[k-1])
      k--
  }
};

// take k elements from the end
// splice mutates array and returns removed items
// add those elements to the front