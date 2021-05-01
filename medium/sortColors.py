'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
'''
nums1 = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
nums2 = [2,0,1]
# Output: [0,1,2]
nums3 = [0]
# Output: [0]
nums4 = [1]
# Output: [1]

# Approach 1: 3-Pointer approach with Python swap 
# "Python swap" unpacks tuple with comma operator and accesses elements in constant time
# One pass, O(n) time, O(1) space
def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    runner = 0
    left = 0
    right = len(nums) - 1
    while runner <= right:  
        if nums[runner] == 0:
            nums[runner], nums[left] = nums[left], nums[runner]
            runner += 1
            left += 1
        elif nums[runner] == 1:
            runner += 1
        else:
            nums[runner], nums[right] = nums[right], nums[runner]
            right -= 1
        # print('END. runner: {}, l: {}, r: {}, nums: {}'.format(runner, left, right, nums))
    return nums

# Approach 2: Python copy with slice syntax [:] to sort in-place
# One pass, O(n) time, O(1) space. Less efficient than 3-pointer because 
# - slicing lists copies the references which costs you overhead memory. 
# - concatenating two lists creates a new list in memory, complexity O(n+m)
def sortColors(nums):
    count0, count1, count2 = 0, 0, 0
    for i in nums:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        elif i == 2:
            count2 += 1

    nums[:] = [0]*count0 + [1]*count1 + [2]*count2
    return nums

sortColors(nums1)