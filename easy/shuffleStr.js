let s = "codeleet"
let indices = [4,5,6,7,0,2,1,3]

// brute force solution #1 
var restoreString = function(s, indices) {
  let pairs = []
  let i = 0
  // push str and index into array of pairs
  while (i < str.length) {
    pairs.push([str[i], index[i]])
    i++
  }
  // sort pairs by index
  pairs.sort((a,b) => {return a[1]- b[1]})
  // return sorted string
  return pairs.map( item => (item[0])).join('')
}

// leetcode voted solution #1
var restoreString = function(s, indices) {
  return indices
      .map((e,i)=>({l: s[i],i: e}))
      .sort((a,b)=>a.i-b.i)
      .map(e=>e.l).join('')
};

// first map returns
// [
//   { l: 'c', i: 4 },
//   { l: 'o', i: 5 },
//   { l: 'd', i: 6 },
//   { l: 'e', i: 7 },
//   { l: 'l', i: 0 },
//   { l: 'e', i: 2 },
//   { l: 'e', i: 1 },
//   { l: 't', i: 3 }
// ]

// leetcode voted solution #2
var restoreString = function(s, idx) {
  const result = [];
  for(let i = 0; i < s.length; i++) {
      result[idx[i]] = s[i]
  }
  return result.join('');
};

// time complexity O(n^2)
// loops through index until str[0] => [ <4 empty items>, 'c', 'o', 'd', 'e' ]
// then fills in the rest 