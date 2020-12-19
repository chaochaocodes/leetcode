
const maxProduct = nums => {
  let max = 0;
  for (let i = 0, j = nums.length - 1; i < j;) {
    max = Math.max(max, (nums[i] - 1) * (nums[j] - 1));
    nums[i] < nums[j] ? ++i : --j;
  }
  return max;
};

var maxProduct = function(nums) {
  nums.sort((a,b)=>b-a);
  return (nums[0]-1)*(nums[1]-1);
};