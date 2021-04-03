# INPUT:  nums: List[int], k: int
# OUTPUT:  None 

# solution using slice and copy
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k + 1
    slice_object = slice(k)
    nums[:] = nums[k:] + nums[slice_object]

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums,k)


# One-liner solution
# nums[:] = nums[len(nums)-k:] + nums[0:len(nums)-k]
