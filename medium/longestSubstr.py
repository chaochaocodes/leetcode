'''
Given a string s, find the length of the longest substring without repeating characters.

** looking for substring NOT subsequence!
'''
s0 = " " # 0
s1 = "abcabcbb" # abc, 3
s2 = "bbbbb" # b, 1
s3 = "pwwkew" # wke, 3 (not pwke, not looking for a subsequence)

# Approach 1: Sliding Window, O(n) time, O(1) space
def lengthOfLongestSubstring(s):
    n = len(s)
    l, r, res = 0, 0, 0
    # use set() to check for repeating characters
    char = set() 

    while r < n:
        if s[r] in char:
            char.remove(s[l])
            l += 1
        else:
            char.add(s[r])
            r += 1
            res = max(res, r - l)
    
    print(res)


# Approach #2: Faster, using hashmap + pointer
def lengthOfLongestSubstring(s):
    if not s: return 0

    d=dict()
    m=0
    j=0
    for i in range(len(s)):
        if s[i] in d and j<=d[s[i]]:
            j=d[s[i]]+1
        else:
            m = max(m,i-j+1)

        # dict keeps track of current letter's index
        d[s[i]]=i
    return m


# Approach 3: Counter() 
# Hash for time/space efficiency,  {char: char_count}
# Worst case is O(2N) = O(N) when all duplicate
from collections import Counter
def lengthOfLongestSubstring(s):
    
    chars = Counter()
    prev, res = 0, 0

    for pos, char in enumerate(s):    
        chars[char] += 1
        while chars[char] > 1:
            chars[s[prev]] -= 1
            prev += 1
        
        res = max(res, pos-prev+1)
    
    return res
            


lengthOfLongestSubstring(s0)


