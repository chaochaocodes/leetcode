# 1. Using dictionary, .items()
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map
        count = dict()
        for i in s:
            count[i] = count.get(i, 0) + 1
        # check if uniq value exists
        if 1 not in count.values():
            return -1
        # find index
        for k,v in count.items():
            if v == 1:
                return s.index(k)
        
# 2. Using collections Counter()
def firstUniqChar(s):
    # build hash map
    count = collections.Counter(s)
    # find index
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx
    return -1
 
# 3. Using .index and .rindex
def firstUniqChar(s):
    for i in range(len(s)):
        # if first index appearance == last index occurence
        if s.index(s[i]) == s.rindex(s[i]):
            return i
            
    return -1

