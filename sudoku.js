const board1 = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

// loop through rows, columns, sub arrays
// push integers to temp array
// if temp array != uniq, return false! 
const isValidSudoku = (board) => {

  // CHECK ROWS [0][0..9]
  let row = 0
  while (row < 9) {
  let rowArray = []
    for (col = 0; col < 9; col++) { 
      if (board[row][col] !== '.') {
        rowArray.push(board[row][col])
      }
    }
    // console.log('rowArray length:', rowArray.length)
    // console.log('new set', new Set(rowArray).size)
    // console.log(rowArray)
    if(new Set(rowArray).size !== rowArray.length) return false
    row++ 
  }

  // CHECK COLUMNS [0..9][0]
  let col = 0
    while (col < 9 ) {
      let colArray = []
        for (row = 0; row < 9; row++) {
          if (board[row][col] !== '.') {
            colArray.push(board[row][col])
          }
        }
      if(new Set(colArray).size !== colArray.length) return false
      col++
    }

  // CHECK SUBARRAY
  // [0..2][0..2], [0..2][3..5], [0..2][6..8]
  // [3..5][0..2], [3..5][3..5], [3..5][6..8]
  // [6..8][0..2], [6..8][3..5], [6..8][6..8]
  for (let row = 0; row < 9; row = row + 3){
      for (let col = 0; col < 9; col = col + 3) {
          let matrix = []
          let subX = row + 3;
          let subY = col + 3;
          // matrix starts at row x until x+3
          for (let x = row; x < subX; x++) {   
              // start at col l unti l+3
              for (let y = col; y < subY; y++) {
                if(board[x][y] !== '.') {
                  matrix.push(board[x][y])
                }
              }
              console.log(matrix)
              if (new Set(matrix).size !== matrix.length) return false
          }
      }
  }
  return true
}

isValidSudoku(board1)

// Other ways: use Map{}
// for (let i = 0; i < board.length; i++){
//   let rowMap = {};
//   for (let j = 0; j < board[0].length; j++){
//       if (board[i][j] === '.') continue;
//       let currentValue = board[i][j];
//       if (rowMap[currentValue] === undefined) {
//           rowMap[currentValue] = currentValue;
//       } else {
//           return false;
//       }
//   }
// }
