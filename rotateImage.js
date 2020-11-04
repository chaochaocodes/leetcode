/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */

// SOLUTION 1
var rotate = function(matrix) {
  let n = matrix.length
  
  // transpose
  for (let i = 0; i < n; i++) {
      for (let j = i; j < n; j++) {
          let temp = matrix[j][i]
          matrix[j][i] = matrix[i][j]
          matrix [i][j] = temp
      }
  }
  
  // reverse each row
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n / 2; j++) {
      let temp = matrix[i][j];
      matrix[i][j] = matrix[i][n - j - 1];
      matrix[i][n - j - 1] = temp;
    }
  }
    
};

// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [[7,4,1],[8,5,2],[9,6,3]]

// Input      Transpose   Output
// [1,2,3]    [1,4,7]     [7,4,1]
// [4,5,6]    [2,5,8]     [8,5,2]
// [7,8,9]    [3,6,9]     [9,6,3]

// SOLUTION 1: transpose
//  ↓ ↓ ↓ 
// [1,2,3]   -> 1
// [4,5,6]   -> 2
// [7,8,9]   -> 3

// SOLUTION 2: transpose
// [1,2,3]   2 <-> 4
// [4,5,6]   3 <-> 7
// [7,8,9]   6 <-> 8

// SOLUTION 2
// var rotate = function(matrix) {
//   for(let i=0;i<matrix.length;i++){
//       for(let j=i+1;j<matrix[i].length;j++){
//           let temp = matrix[i][j]
//           matrix[i][j] = matrix[j][i]
//           matrix[j][i] = temp
//       }
//   }
//   for(let i=0;i<matrix.length;i++){
//       matrix[i].reverse()
//   }  
// };