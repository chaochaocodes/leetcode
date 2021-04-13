from collections import Counter 

# 1. Use Counter
def containsDuplicate(nums):
    count = Counter(nums)
    for i in count:
        if count[i] > 1:
            return True
            
# # 2. Use set()
# def containsDuplicate(self, nums: List[int]) -> bool:
#     nset = set(nums)
#     if len(nset) < len(nums):
#         return True
#     return False


nums1 = [1,2,3,1] # true
nums2 = [1,2,3,4] # False
containsDuplicate(nums2)