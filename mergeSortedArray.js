// Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

// Note:
// The number of elements initialized in nums1 and nums2 are m and n respectively.
// You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
// Example:

// Input:
// nums1 = [1,2,3,0,0,0], m = 3
// nums2 = [2,5,6],       n = 3

// Output: [1,2,2,3,5,6]
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
// cannot use concat or spread => creates new array
// .flat() not a recognized function here
// must add nums2 into nums1 array! 

var merge = function(nums1, m, nums2, n) {
  for (i = 0; i < n; i++) {
    nums1[m + i] = nums2[i]
  }
  return nums1.sort((a,b) => a - b)
};