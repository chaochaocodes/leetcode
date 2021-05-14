'''
https://leetcode.com/problems/move-zeroes/
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''
nums = [0,1,0,3,12] #Output: [1,3,12,0,0]
nums1 = [0] #Output: [0]

# Move in-place with Python swap
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    zeroPosition = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i],nums[zeroPosition] = nums[zeroPosition],nums[i]
            zeroPosition += 1
    return nums