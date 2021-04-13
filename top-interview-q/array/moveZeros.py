# Testcases
nums = [0,1,0,12,3] #[1,12,3,0,0]
nums = [0]          #[0]

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Two Pointer Technique and Python list swap
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



# Sort by key and reverse parameters
def moveZeros(nums):
  # nums.sort(reverse=True)     #[12, 3, 1, 0, 0]
  # nums.sort(key=bool)         #[0, 0, 1, 12, 3]
  nums.sort(reverse=True, key=bool) # [1, 12, 3, 0, 0]