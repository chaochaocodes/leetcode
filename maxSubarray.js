// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.

// Synopsis:
// At each ending index i, we have 2 choices. Choose the maximum result:
// Case 1: append A[i] onto the ongoing subarray sum by adding A[i] onto sum
// Case 2: start a new subarray at A[i] by setting sum equal to A[i]
// Track and return the maximum max of each subarray sum ending at each index i.

var maxSubArray = (nums) => {    
  let sum = nums[0]
  let max = nums[0]
  for (i=0; i<nums.length; i++){
    sum = Math.max(sum + nums[i], nums[i])
    max = Math.max(max, sum)
  }
  return max
};