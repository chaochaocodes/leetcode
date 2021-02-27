/**
 * @param {number[]} height
 * @return {number}
 */
// https://leetcode.com/problems/container-with-most-water/

var maxArea = function(height) {
  // start with widest width and work inwards
  let w = height.length-1
  let l = 0
  let area = 0

  while (l < w) {
      // find area using shorter line * width-1
      area = Math.max(area, Math.min(height[l],height[w]) * (w-l));
      
      if (height[l] < height[w]) 
          l++;
      else
          w--;
  }
  return area
};