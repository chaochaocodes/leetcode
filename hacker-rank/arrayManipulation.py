'''
HackerRank:  Hard
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.  Example:

n = 10
queries = [[1,5,3], [4,8,7], [6,9,1]]

a b k
1 5 3
4 8 7
6 9 1

Values of k between indices a, b inclusive
 1 2 3  4  5 6 7 8 9 10  <---index
[0,0,0, 0, 0,0,0,0,0, 0]  start with 1-indexed array of zeros
[3,3,3, 3, 3,0,0,0,0, 0]  from 1 to 5 inclusive, add 3
[3,3,3,10,10,7,7,7,0, 0]  from 4 to 8 inclusive, add 7
[3,3,3,10,10,8,8,8,1, 0]  from 6 to 9 inclusive, add 1

Max value = 10
'''

'''
Approach 1: Good Solution
Loop over rows in query, sub-loop over elements of array that need summation.
However will not pass higher tests when n is very large
Accessing every element the query would modify takes too much time
'''
def arrayManipulation(n, queries):
    # loop queries, add and save k values to an array, return max
    f = [0]*n
    q = len(queries)
    # for each query, from index 0 to 1, add index 2
    for i in queries:
      for j in range(i[0]-1, i[1]):
        f[j] += i[2]
    return max(f)


'''
Approach 2. Best Solution
Key insight:  the sum only needs to be calcuated for each STEP or FALL in the array rather than every individual element.  This allows us to do a single loop for calculating the two steps in the array, and another for the maximum step height.

Using the example, the array of steps and falls is:
[3, 0, 0, 7, 0, -2, 0, 0, -7, -1, 0]

Print running_count to see that it's identical to the final array of summations.
[3, 3, 3, 10 ,10, 8, 8, 8, 1, 0]

Edge-case: the FALL is calculated after the element, so if a == len(arr), then arr[b] -= k will return "IndexError: list index out of range"
Two options: 
1.  Initiate array as arr = [0] * n + 1
2.  Add conditonal --- if b != len(arr), then arr[b] -= k

'''
def arrayManipulation(n, queries):
    array = [0] * (n+1)

    # Save interval endpoint's "k" values in array
    for query in queries: 
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k

    # Find max value
    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        print('running count: {}, max: {}'.format(running_count, max_value))
        if running_count > max_value:
            max_value = running_count

    print(array)
    return max_value


n1 = 10 # max = 10
queries1 = [[1,5,3], [4,8,7], [6,9,1]]

n2 = 5 # max value = 200
queries2 =[[1, 2, 100], [2, 5, 100], [3, 4, 100]]
arrayManipulation(n, queries)