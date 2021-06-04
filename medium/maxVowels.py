'''
Given a string s and an integer k.
Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''

s = "leetcode"
k = 3 # Output 2

# # Approach 1: Sliding Window, intuitive -- Exceeds Time Limit!
# def maxVowels(s, k):
#     # sliding window of length k
#     # count number of vowels, save as max
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     l = 0
#     r = l+k
#     v,m = 0, 0
    
#     while r < len(s):
#         for i in range(l,r):
#             if s[i] in vowels:
#                 v += 1  
#         l += 1
#         m = max(m, v)       
#     print(m)



# Approach 2: Sliding Window, count vowels we gain/lose
def maxVowels(s, k):
    vowels = 'aeiou'
    n = len(s)
    
    if n < k:
        return -1

    # find no. of vowels in first window
    v = 0  # current count of vowels
    for i in range(k):
        v += 1 if s[i] in vowels else 0

    m = v  # max vowels
    for i in range(k,n):
        v += ((1 if s[i] in vowels else 0) - (1 if s[i-k] in vowels else 0))
        m = max(m,v)

    print(m)


# Approach 3:  Sliding Window + enumerate
def maxVowels(s, k):
    # Maximum vowels i.e. ans
    ans: int = 0
    
    # Vowels in current window
    currCount: int = 0
        
    # String of vowels
    vowels: str = "aeiou"
        
    # Using sliding window technique to 
    # calculate number of vowels in each window and 
    # update the count
    for i, v in enumerate(s):
        if i >= k:
            if s[i-k] in vowels:
                currCount -= 1
        if s[i] in vowels:
            currCount += 1
        ans = max(currCount, ans)
    return ans

maxVowels(s,k)
