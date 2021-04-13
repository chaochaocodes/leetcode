/**
 * @param {number[]} nums
 * @return {boolean}
 */

// 1. Solution with sort and For loop
 var containsDuplicate = function(nums) {
    // edge case
    if (nums === null || nums === []) return false
    // clone array to avoid modifying input
    let sorted = [...nums].sort()
    // any duplicate int will be consecutive after sorting
    for (i = 0; i < sorted.length; i++) {
        if (sorted[i] == sorted[i + 1]) return true;             
    }
    return false;
};


// 2. Solution with Set()
var containsDuplicate = function(nums) {
    return nums.length !== [...new Set(nums)].length
};

// 3. Solution with hash table
var containsDuplicate = function(nums) {
    const hash = {}
    for (let i = 0; i < nums.length; i++) {
        if (!hash[nums[i]]) {
            hash[nums[i]] = 1
        } else {
            return true
        }
    }
    return false
};