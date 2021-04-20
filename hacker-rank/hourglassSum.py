def hourglassSum(arr):
    maxsum = -63
    for i in range(4):
        for j in range(4):
            hourglass = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            maxsum = max(maxsum, hourglass)

    return maxsum


ex1 = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
print(hourglassSum(ex1))

# hourglass indices:

# [0][0]  [0][1]  [0][2]
#         [1][1]
# [2][0]  [2][1]  [2][2]

# [i][j] + [i][j+1] + [i][j+2]
#         [i+1][j+1]
# [i+2][j]  [i+2][j+1]  [i+2][j+2]

# 1. sum indices
# 2. loop through matrix 6 * 6
# 3. return max sum

# ex1 = [
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0 ]
# output: 19

# Constraints
# -9 <= arr[i][j] <= 9  ---> -9 * 7 indices (per hourglass) => initialize maxsum to -63
#  0 <= i,j <= 5

