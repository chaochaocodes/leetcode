# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

# 1. Dictionary
def singleNumber(nums):
    numsdict = dict()
    for number in nums:
        numsdict[number] = numsdict.get(number, 0) + 1
    print(numsdict)
    
    for k,v in numsdict.items():
        if v == 1: 
            return k

# Leetcode appraoch #2: Hash Table
from collections import default dict

def singleNumber(nums):
    hash_table = defaultdict()
    for i in nums:
        hash_table[i] += 1

    for i in hash_table:
        if hash_table[i] == 1:
            return i   

# Time complexity : O(n \cdot 1) = O(n)O(n⋅1)=O(n). Time complexity of for loop is O(n)O(n). Time complexity of hash table(dictionary in python) operation pop is O(1)O(1).

# Space complexity : O(n)O(n). The space required by hash\_tablehash_table is equal to the number of elements in \text{nums}nums.


# Leetcode Approach #3: Math
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return 2 * sum(set(nums)) - sum(nums)

# Time complexity : O(n + n) = O(n)O(n+n)=O(n). sum will call next to iterate through \text{nums}nums. We can see it as sum(list(i, for i in nums)) which means the time complexity is O(n)O(n) because of the number of elements(nn) in \text{nums}nums.

# Space complexity : O(n + n) = O(n)O(n+n)=O(n). set needs space for the elements in nums



nums1 = [2,2,1] #1
nums2 = [4,1,2,1,2] #4
nums3 = [1] #1

singleNumber(nums1)