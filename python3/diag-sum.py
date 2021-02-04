'''
Given square matrix mat, return sum of primary matrix diagonals.
Only include each cell once. (In odd size matrices, center cell overlaps)

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
'''

def diagonalSum(A):
  n   = len(A)
  res = 0
  for i in range(n):
      res += A[i][i] + A[i][n-1-i]
  # x: Index of Element Repeated (when n is Odd)
  x = (n-1)//2
  return res - A[x][x] if n&1 else res


if __name__ == '__main__':
  mat = [[1,2,3], [4,5,6], [7,8,9]] # res: 25
  # mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]] # res: 8
  # mat = [[5]] # res: 5
  print(diagonalSum(mat))


  # sum=0
  # for i in range(0,len(mat)):             #rows
  #     for j in range(0,len(mat[0])):      #col
  #         if(i+j==(len(mat)-1) or i==j):  # L and R diag
  #             sum=sum+mat[i][j]
  # return sum