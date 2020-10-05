/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

var twoSum = function(nums, target) {
  for (i=0; i < nums.length; i++) {
    for (j=0; j < i; j++) {
      if (nums[j]+ nums[i] == target) return [j, i]
      }
    }
};