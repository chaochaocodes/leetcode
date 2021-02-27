# Example Input, Output: [4,9]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

import collections
# 1. Using map, collections.Counter, list
def intersect(self, nums1, nums2):
    a, b = map(collections.Counter, (nums1, nums2))
    return list((a & b).elements())

# 2. Variations
def intersect(nums1, nums2):
    C = collections.Counter
    return list((C(nums1) & C(nums2)).elements())

    # print(C)
    # # <class 'collections.Counter'>
    # print(C(nums1))
    # # Counter({4: 1, 9: 1, 5: 1})
    # print(C(nums2))
    # # Counter({9: 2, 4: 2, 8: 1})

        # print(C(nums1) & C(nums2))
        # # Counter({4: 1, 9: 1})
        # print((C(nums1) & C(nums2)).elements())
        # # <itertools.chain object at 0x1077f0fd0>
    
    # print(list(C(nums1) & C(nums2)))
    # # [4, 9]
    # print(list((C(nums1) & C(nums2)).elements()))
    # # [4, 9]


intersect(nums1, nums2)

# 3. Variation
# def intersect(self, nums1, nums2):
#     return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())