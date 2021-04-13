# How to keep track of sub boxes?
# box_index = (row / 3) * 3 + col / 3

# Complexity Analysis
# Time complexity : O(1), one iteration over the board of 81 cells
# Space complexity : O(1)

# Solution with Dict and get()
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

# i = 2
# j = 2
# box_index = (i//3) * 3 + (j//3)
# print(box_index)

# Solution using Set and List
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        list1 = [set() for _ in range(9)]
        list2 = [set() for _ in range(9)]
        list3 = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if not board[i][j].isnumeric():
                    continue
                # box index
                y = i // 3
                x = j // 3
                num = board[i][j]
                # check if value already exists
                if (num in list1[i]) or (num in list2[j]) or (num in list3[x][y]):
                    return False
                # save value to list 
                else:
                    list1[i].add(num)
                    list2[j].add(num)
                    dic_list3[x][y].add(num)
        return True