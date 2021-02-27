/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */

// Given two arrays, write a function to compute their intersection.

// Example 1:

// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2,2]
// Example 2:

// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [4,9]


var intersect = function(nums1, nums2) {   
  nums1.sort((a,b) => a-b)
  nums2.sort((a,b) => a-b) 
  let result = []
  i=0
  j=0

  while ( i < nums1.length && j < nums2.length) {
      if (nums1[i] == nums2[j]) {
        result.push(nums1[i])
        i++ 
        j++
      } else if (nums1[i] < nums2[j]) {
          i++
      } else {
          j++
      }
  }
  return result;
};
