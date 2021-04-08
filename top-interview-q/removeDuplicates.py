
# Two-Pointer 
def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            # copy value of next unique number into position
            # array size unchanged
            nums[i] = nums[j]
    return i + 1

# Two-Pointer variation
def removeDuplicates(self, nums: List[int]) -> int:
    
    i = 0
    while i < (len(nums)-1):
        if nums[i] == nums[i+1]:
            # remove duplicate numbers; array size reduced 
            nums.remove(nums[i])
        else:
            i += 1
    return len(nums) 

# Simple
def removeDuplicates(nums):
    # index slicing - copies references to objects in the list, it does not generate a new object
    # set 'reference copy' to set(nums) for unique values
    # sorted() converts set {} back to list []
    nums[:] = sorted(set(nums))
    return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)