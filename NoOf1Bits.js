// Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

// Example 1:

// Input: 00000000000000000000000000001011
// Output: 3
// Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
  return n.toString(2).split('0').join('').length;
};

// 1) n.toString(2) converts n into binary string
// 2) split('0') returns an array of the binary string 
// splitting only at 0's and  returning an array of only 1 present in binary of n
// 3) join('') joins all 1s and returns a string of 1s
// 4) length finds length of the string, counting number of 1's in n.