def rotate(matrix):
    n = len(matrix)

    # transpose
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # reflect
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

    # for i in range(n):
    #     matrix[i].reverse()


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Input      Transpose   Reflect
# [1,2,3]    [1,4,7]     [7,4,1]
# [4,5,6]    [2,5,8]     [8,5,2]
# [7,8,9]    [3,6,9]     [9,6,3]

# Transpose on diagonal
# [1,2,3]   2 <-> 4
# [4,5,6]   3 <-> 7
# [7,8,9]   6 <-> 8

# Transpose on diagonal
# [1,2,3]   2 <-> 4
# [4,5,6]   3 <-> 7
# [7,8,9]   6 <-> 8