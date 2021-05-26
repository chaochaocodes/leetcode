'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

'''
numss = [4,3,2,7,8,2,3,1] # [5,6]

# Approach 1
# Intuitive: Compare unique values, return difference
# Time:  O(n) to find different between sets, where n = length of longer set, which in this case is len(nums)
def findDisappearedNumbers(nums):
    n = len(nums)
    setRange = set(range(1,n+1))
    setNums = set(nums)
    return setRange - setNums

# Approach 2
# Without extra space and O(n) runtime
# We go through the array, and in the place of the given value, we can change its sign. 
# Now we can find and return where the index has not changed.
def findDisappearedNumbers(nums):
    for i in range(len(nums)):
        nums[abs(nums[i]) - 1] = - abs(nums[abs(nums[i]) - 1])
    return [i+1 for i in range(len(nums)) if nums[i] > 0]


findDisappearedNumbers(numss)
