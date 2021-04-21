'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example: 
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Tip: Think about how we can calculate the i-th number in the running sum from the (i-1)-th number.
'''

# Approach 1:  Brute Force
# Complexity:  O(n) time / O(n) space
def runningSum(self, nums: List[int]) -> List[int]:
    res = []
    total = 0
    
    for i in nums:
        total += i
        res.append(total)
        
    return res


# Approach 2: DP, memoization
# Complexity: O(n) time / O(1) space 
# O(1) space since no additional space is used to find the running sum.  
# *Note that doesn't take into consideration the space occupied by the output array*
def runningSum(self, nums: List[int]) -> List[int]:

    res = []
    
    for i in range(len(nums)):
        res[i] = nums[i] + res[i-1]
        
    return res

# Approach 3:  Using sum() and slice[:]
# Complexity: O(n) time / O(1) space
def runningSum(self, nums: List[int]) -> List[int]:
    res = []
    curr = 1
    while len(res) != len(nums):
        res.append(sum((nums[0:curr])))
        curr += 1
    return res

# Approach 4:  Using input Array for Output
# Complexity: O(n) time / O(1) space
def runningSum(self, nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        # Result at index `i` is sum of result at `i-1` and element at `i`
        nums[i] += nums[i-1]
        return nums 