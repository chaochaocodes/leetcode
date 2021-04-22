n = 5 # max value: 200
query = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

# Queries:
# a b k
# 1 2 100
# 2 5 100
# 3 4 100
# Values of k between indices a,b inclusive
# 100 100   0   0   0
# 100 200 100 100 100
# 100 200 200 200 100

def arrayManipulation(n, queries):
    # dynamic programming!!  
    # loop queries, add and save k values to an array, return max
    f = [0]*n
    q = len(queries)
    # for each query, from index 0 to 1, add index 2
    for i in queries:
        start = i[0]-1
        print('i: {}'.format(i))
        while start < i[1]:
            # print('start: {}, end: {}'.format(start, i[1]))
            f[start] += i[2]
            start += 1
    
    # print(f)
    return max(f)

n = 5
queries =[[1, 2, 100], [2, 5, 100], [3, 4, 100]]
arrayManipulation(n, queries)