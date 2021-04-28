'''
Given a string s, find the length of the longest substring without repeating characters.

** looking for substring NOT subsequence!
'''
s0 = " " # 0
s1 = "abcabcbb" # abc, 3
s2 = "bbbbb" # b, 1
s3 = "pwwkew" # wke, 3 (not pwke, not looking for a subsequence)

def lengthOfLongestSubstring(s):
# sliding window!  O(n) time, O(1) space
# use set() to check for repeating characters
# hashmap for time/space efficiency,  {set(substr): len(substr)}
    n = len(s)
    l, r, res = 0, 0, 0
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

# Faster approach
class Solution(object):
    def lengthOfLongestSubstring(self, s):
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

lengthOfLongestSubstring(s0)