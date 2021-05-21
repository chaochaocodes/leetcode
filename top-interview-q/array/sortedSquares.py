'''
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, 
could you find an O(n) solution using a different approach?
'''
nums0 = [-4,-1,0,3,10] # squared [16,1,0,9,100] => sorted [0,1,9,16,100]
nums1 = [-7,-3,2,3,11] # [4,9,9,49,121]

# Approach 1:  Brute force
# Time: O(log n) + O(n log(n)) = O(n log(n))
# *Python sort uses Timesort algo O(nlogn)
# Space: O(n)
def sortedSquares(nums):
    return sorted([x**2 for x in nums]) # squaring = O(log n)

def sortedSquares(nums):
    return sorted([x*x for x in nums]) # naive multiplication = O(n)


# Approach 2:  Two-pointer using deque()
# Time/Space:  O(n)
from collections import deque
def sortedSquares(nums):
    if not nums: return []
    output = deque()
    n = len(nums)
    l,r = 0,n-1
    while l <= r:
        lVal, rVal= abs(nums[l]), abs(nums[r])
        if lVal >= rVal:
            output.appendleft(lVal ** 2)
            l+=1
        else:
            output.appendleft(rVal ** 2)
            r-=1
    return output

# Approach 3:  Stack array
# Time/Space:  O(n)
# Append negative elements to a stack
# Once you encounter non-negative elements, clear the stack by comparing the current element to the last value in the stack, then append squared value to output array. 
# If all elements in nums have been seen, clear the stack by appending squared value to output.
def sortedSquares(nums):
    stack = []
    output = []
    for i in range(len(nums)):
        if nums[i] < 0:
            stack.append(-nums[i])
        else:
            while stack and stack[-1] < nums[i]:
                output.append(stack.pop() ** 2)
            output.append(nums[i] ** 2)
    while stack:
        output.append(stack.pop() ** 2)
    return output


sortedSquares(nums0)