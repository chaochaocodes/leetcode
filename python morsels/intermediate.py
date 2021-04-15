# 1. Add matrices without libraries 
# [0][0], [0][1]    [1][0], [1][1]
def add(matrix1, matrix2):
    for i in range(len(matrix1)):      # outer list
    for j in range(len(matrix1[0])): # inner list
        matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    print(matrix)

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
# [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
add(matrix1, matrix2)


# 2. Parse given ranges into list
def parse_ranges(str_range):
  split_str = str_range.split(',')
  result = []
  for i in split_str:
    x,y = i.split('-')
    x,y = int(x), int(y)    
    for j in range(x,y+1):
      result.append(j)
      print(result)

parse_ranges('1-2,4-4,8-10')
# [1, 2, 4, 8, 9, 10]
# parse_ranges('0-0, 4-8, 20-20, 43-45')
# [0, 4, 5, 6, 7, 8, 20, 43, 44, 45]


# 3.  Make an Ordered Set class without using set()
# This class should work like a set, but it should also maintain the insertion order of the items added to it (unlike Python's built-in set which is unordered).

def OrderedSet(ordered_words):
  result = []

  for i in ordered_words:
    if i in result:
      continue
    result.append(i)

  for i in result:
    print(i, end=" ")

  return result

ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']
print(*set(ordered_words))
# Output:  an words in these are order
print(*OrderedSet(ordered_words))
# Output:  these are words in an order
print(*OrderedSet(['repeated', 'words', 'are', 'not', 'repeated']))
# Output:  repeated words are not

# This set should be relatively memory efficient and containment checks should be relatively time efficient:
words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
print(len(words)) #4
print('hello' in words) # True
# Initially you don't have to worry about allowing sets to be modified after they've been made. Just focus on getting len and the in operator.

