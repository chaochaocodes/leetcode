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
  matrix = [[0 for x in range(n)] for y in range(3)]
  print(queries)

  test = []
  for y in range(3):
    row = []
  # loop through queries to set range(start/stop)
    start = queries[y][0]-1
    stop = queries[y][1]
    k = queries[y][2]
    print('start: {}, stop:{}, k:{}'.format(start, stop, k))
    
    for x in range(n):
      if x >= start and x < stop:
        row.append(k)
      else:
        row.append(0)
    test.append(row)

    for i in test:
      print(i)

print(arrayManipulation(n, query))