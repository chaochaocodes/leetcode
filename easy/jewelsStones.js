// Find the number of Jewels in Stones
// J = "aA", S = "aAAbbbb" // 3
// numJewelsInStones(J, S)

// brute force solution
var numJewelsInStones = function(J, S) {
  let result = {}
  // create keys in result from types of Jewels
  for(let j in J){
    hash[J[j]] = 0
  }
  // check for keys (jewels) that exist in stones
  // if key exists, value +=1
  for (const k in result) {
    let i = 0
    while (i < S.length) {
      if (k == S[i]) {result[k] += 1}
      i++
    }
  }
  console.log(result)

  // sum of values in result
  let totalJewels = 0
  for (const value in result) {
    totalJewels += result[value]
  }

  return totalJewels
};

// Solution #2: {}
var numJewelsInStones = function(J, S) {
  let hash = {};
  let count = 0;
  for(let j in J){
      hash[J[j]] = j
  }
  for(let i in S){
      if(hash[S[i]]){
          count++
      }
  }
  return count
};


// Solution #3:  indexOf, charAt
var numJewelsInStones = function(J, S) {
  let result = 0;
  for(let i = 0; i < S.length; i++) {
      if(J.indexOf(S.charAt(i)) >= 0)
          result++;
  }
  return result;
};