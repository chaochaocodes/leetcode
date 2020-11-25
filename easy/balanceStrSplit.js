// Solution #1: if/else matches of 'RLRRRLLL'
// Time: O(n)
// Space: O(1)
var balancedStringSplit = function(s) {    
  let count = 0;
  let match = 0;

	for (let i = 0; i < s.length; i++) {

		if (s[i] === "R") {
			count++ // count += 1
		} else if (s[i] === "L") {
			count-- // count -= 1
		}

		if (count === 0) {
			match++
		}
	}
	return match;
};

// Solution #2: for any 2 letters, compared to str[0]
var balancedStringSplit = function(s) {    
  let count=1;
  let result=0;
  for (let i=1; i<s.length; i++) {
      s[i] == s[0]? count++ : count--;
      if (count == 0)
          result++;
  }
  return result;
};

// Solution #3: map
var balancedStringSplit = function(s) {
  let count = 0
  let match = 0
  s.split('').map(c => {
      if (c === "R") count++
      if (c === "L") count--
      if (count === 0) match++
  })
  return match
};

// SOLUTION #4: stack data structure.
// Time: O(n)
// Space: O(n)
var balancedStringSplit = function(s) {
    
  let matches = 0;
	const stack = [];

	stack.push(s[0]);

	for (let i = 1; i < s.length; i++) {

		const top = stack[stack.length - 1];

		if (top !== undefined && top !== s[i]) {
			stack.pop()
		} else {
			stack.push(s[i]);
		}

		if (stack.length === 0) {
			matches += 1;
		}
	}

	return matches;
};

// Solution #5: recursion
// The question
var balancedStringSplit = function(s) {
  return countOfBalStr(s, 0)
};

// The recursive tail-call function
function countOfBalStr(string, position, count = null, total = 0) {
  if (position >= string.length) {
      return total
  }
  
  const letter = string[position]
  const value = letter === 'L' ? 1 : -1 // We can hard code this cause this is a contraint on the question
  count += value
  
  if (count === 0) {
      total++
  }
  
  return countOfBalStr(string, position + 1, count, total)
}

// Solution #5: 1-line recursive Solution
const balancedStringSplit = (s, l = 0, r = 0, cnt = 0) =>
!s.length
  ? cnt
  : balancedStringSplit(
      s.slice(1),
      l + +('L' === s[0]),
      r + +('R' === s[0]),
      cnt + +(l === r),
    );