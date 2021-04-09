# How to keep track of sub boxes?
# box_index = (row / 3) * 3 + col / 3
# Complexity Analysis

# Time complexity : O(1), one iteration over the board of 81 cells
# Space complexity : O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initiate data
        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate board, i = row, j = col
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i//3) * 3 + (j//3)

                    # save cell value to dict
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[i].get(num, 0) + 1

                    # check if value already exists
                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_index][num] > 1:
                        return False

        return True

i = 2
j = 2
box_index = (i//3) * 3 + (j//3)
print(box_index)
