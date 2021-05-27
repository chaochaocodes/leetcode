'''
Given integer array nums, return the third maximum **distinct** number in this array. If the third maximum does not exist, return the maximum number.

'''
nums = [2,2,3,1] # Output: 1

# Time complexity:  O(n)
# Space complexity: O(n1)
def thirdMax(nums):
    unique = sorted(set(nums))
    length = len(unique)
    if length >= 3:
        return unique[length-3]
    else:
        return max(unique)

# Written as 3 lines
def thirdMax(nums):
    if len(set(nums)) < 3:
        return max(nums)
    return sorted(list(set(nums)))[-3]