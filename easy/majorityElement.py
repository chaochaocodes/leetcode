'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
nums1 = [3,2,3] #3
nums2 = [2,2,1,1,1,2,2] #2


# Approach 1: Brute force
# Time: O(n^2), 2 nested for loops
# Space: O(1)
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

# Approach 2: Hash map
# Time: O(n), Counter maps elements in linear time
# Space: O(n)
import collections
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# Approach 3: Sorting
# Intuition: If elements are sorted, the majority element can be found at n/2 or n/2 + 1 (if n is even).
# Time: O(nlgn), Sorting the array costs O(nlogn) in Python
# Space: O(1) if sorted in place, else O(n) for a copy of nums to sort

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]