'''
Find number that appears once in array
'''

# Approach 1: Hash table
# Time: O(n), for-loop runtime is O(n); hash table operation is O(1)
# Space: O(n), space required in hash table is n elements in nums
def singleNumber(nums):
    numsdict = dict()
    for i in nums:
        numsdict[i] = numsdict.get(i, 0) + 1
    
    for k,v in numsdict.items():
        if v == 1: 
            return k
            
# Approach 2: Math
# Concept: 2*(a+b+c)-(a+a+b+b+c) = c
# Time: O(n+n) = O(n)
# sum will call 'next' to iterate through nums, aka sum(list(i, for i in nums)), so time complexity is O(n) for n elements in nums
# Space: O(n+n) = O(n)
# set() needs space for the elements in nums
def singleNumber(nums):
    return 2 * sum(set(nums)) - sum(nums)
