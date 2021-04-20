# Test Case file: input08, Expected Output: 9984

# Approach 1: Loop and Swap minimum value
# Result: 5/15 test case = Time limit exceeded -- finding index takes too long!
def minimumSwaps(arr):
    sorted_arr = sorted(arr)
    swap = 0
    for i, v in enumerate(arr):
        if arr[i] != sorted_arr[i]: 
            index_min = arr[i:].index(min(arr[i:]))
            arr[i], arr[index_min+i] = arr[index_min+i], arr[i]
            swap += 1
    print(swap, arr)


# Approach 2:  Swap
# All test cases passed!
# arr before [4, 3, 1, 2] 042
# arr after  [2, 3, 1, 4] 023
# arr after  [3, 2, 1, 4] 031
# arr after  [1, 2, 3, 4] 
def minimumSwaps(arr):
    var = 0
    cnt = 0
    n = len(arr)

    while var < n:              
        if arr[var] != (var+1):
            # print('swap: {}, {}'.format(arr[var], arr[arr[var]-1]))
            # nested arr doesn't keep its original value! save to new variables
            p1 = var
            p2 = arr[var]-1
            arr[p1], arr[p2] = arr[p2], arr[p1]
            cnt += 1
            var -= 1

        var += 1

    print(cnt)


# Approach 3:  Loop, Compare with reference array, and Swap with Dict lookup
# Result: 6/15 test cases = Runtime Error
# def minimumSwaps(arr):
#     ref_arr = sorted(arr)
#     index_dict = {v: i for i,v in enumerate(arr)}
#     swaps = 0
#     for i,v in enumerate(arr):  # i = 2, v = 5
#         if v != ref_arr[i]: # if 5 != 3, find index of 3 in dict
#             # find index of correct value to swap with
#             correct_idx = index_dict[ref_arr[i]]    # correct = 3
#             arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
#             # update dictionary
#             index_dict[v] = correct_idx
#             index_dict[arr[i]] = i
#             swaps += 1
            
#     return swaps

# Approach 4: Compare with ref array, and find next index to swap with 
# Result: 6/15 test cases = Runtime Error
# def minimumSwaps(arr):
#     swaps = 0
#     n = len(arr)
#     while arr != [n for n in range(1, n + 1)]:
#         for i in range(n):
#             if (i + 1) != arr[i]:
#                 ni = arr[i] - 1
#                 arr[i], arr[ni] = arr[ni], arr[i]
#                 swaps += 1
#                 i -= 1
#     return swaps



test1 = [4,3,1,2] #3
test2 = [1, 3, 5, 2, 4, 6, 7] #3
print(minimumSwaps(test1))

# if __name__ == '__main__':
#     fptr = open('minSwaps_input08.txt', 'w')
#     n = int(input())
#     arr = list(map(int, input().rstrip().split()))
#     res = minimumSwaps(arr)
#     fptr.write(str(res) + '\n')
#     fptr.close()