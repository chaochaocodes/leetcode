var majorityElement = function(nums) {
  // loop through array of size n
  // count number of times each element appears, save in hash
  // find majority element: el that appears more than n/2 times
  let n = nums.length
  let hash = {}

  for (i=0; i<n; i++) {
      // if hash[arr[i]] doesn't exist, set = 1
      // if hash[arr[i]] exists, value++
      if (nums[i] in hash) {
          hash[nums[i]] += 1
      } else { hash[nums[i]] = 1}
  }
  console.log(hash)

  // return max value
  let max = Math.max(...Object.values(hash))
  console.log(max)

  // find keys in obj, return key of max value
  for (const key in hash) {
    // console.log(key)
    if (hash[key] === max) return key
  }

};


majorityElement([3,2,3]) // 3