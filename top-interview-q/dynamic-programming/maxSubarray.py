def maxSubArray(nums):
    if not nums: 
        return 0
        
    local_max, global_max = 0, None
    for num in nums:
        global_max = max(global_max, local_max+num)
        local_max = max(0, local_max+num)
    return global_max


# one line form
def maxSubArray(nums):
    return reduce(lambda (g,l),x: (max(g,l+x),max(l+x,0)), nums, (None,0))[0]

# dynamic programming
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_so_far, curr_sum = -2**31, 0
    for i in range(len(nums)):
        if curr_sum+nums[i] < 0:
            curr_sum, max_so_far = 0, max(max_so_far, nums[i])
        else:
            curr_sum, max_so_far = curr_sum + nums[i], max(max_so_far, curr_sum + nums[i])
    return max_so_far
