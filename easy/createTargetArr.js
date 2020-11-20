// Given two arrays of integers nums and index. Your task is to create target array under the following rules:

// Initially target array is empty.
// From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
// Repeat the previous step until there are no elements to read in nums and index.
// Return the target array.

// It is guaranteed that the insertion operations will be valid.

// Example 1:

// Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
// Output: [0,4,1,3,2]
// Explanation:
// nums       index     target
// 0            0        [0]
// 1            1        [0,1]
// 2            2        [0,1,2]
// 3            2        [0,1,3,2]
// 4            1        [0,4,1,3,2]

var createTargetArray = function(nums, index) {
  let target = []
  
  for (let i=0; i < nums.length; i++) {
      // insert nums[i] at index[i] of target
      // target[index[i]] = nums[i]
      // target[0] = 0    [0]
      // target[1] = 1    [0,1]
      // target[2] = 2    [0,1,2]
      // target[2] = 3    [0,1,3] ** splice in 3 instead of replace
      // target.splice(2,0,3) <-- at 2, remove 0 el, insert 3
      // target.splice(index[i], 0, nums[i])
      // target[2] = 3    [0,1,3,2]
      // target.splice(index[i], 0, nums[i])
      // target.splice(1, 0, 4)   [0,4,1,3,2]
      target.splice(index[i], 0, nums[i])
  }    
  return target
};

// Option 2:  replace For Loop with for...in
//   for(const i in nums) target.splice(idx[i], 0, nums[i])
