
// LOOP solution
var kidsWithCandies = function(candies, extraCandies) {
  // if candies + extraCandies < mostCandies, return false
  // if candies + extraCandies >= mostCandies, return true
  // find max candies for comparison
  let result = []
  for (let i=0; i<candies.length; i++){
    candies[i] + extraCandies < Math.max(...candies) ? result.push(false) : result.push(true)
  }
  return result
};

// ONE LINER w MAP
var kidsWithCandies = (candies, extraCandies) => candies.map((v) => (v + extraCandies) >= Math.max(...candies))


// candies = [2,3,5,1,3], extraCandies = 3
// [true,true,true,false,true] 
kidsWithCandies(candies, extraCandies)