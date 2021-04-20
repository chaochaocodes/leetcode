'''
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

Example
'abc'
This is a valid string because frequencies are {a:1, b:1, c:1}
'abcc'
This is a valid string because we can remove one 'c'.
'''

s0 = 'aabbc' # Yes (if you remove c, then a:2, b:2)
s1 = 'aabbcd' # No
s2 = 'aabbccddeefghi' # No

# Checking edge cases
v1 = [2, 2, 1, 1] # No  -- 
v2 = [1, 2, 1, 1] # Yes -- if all, or all but 1 == minimum, YES because 2-1 = 1 == same frequency
v3 = [2, 2, 2, 1] # Yes -- if all, or all but 1 == maximum, YES, by removing the 1
v3 = [3, 2, 2, 1] # No

from collections import Counter
def somefunction(s):
    s = Counter(s)
    minVal = min(s.values())
    maxVal = max(s.values())

    check_min = {k:v for k,v in s.items() if v == minVal}
    check_max = {k:v for k,v in s.items() if v == maxVal}

    if (sum(s.values()) - (sum(check_min.values()) + minVal) <= 1):
      print('inside min YES')
    elif (sum(s.values()) - sum(check_max.values()) <= 1):
      print('YES')
    else:
      print('NO')

    for i in s:
      print('s:', i, s[i])
    print()
    for i in check_max: 
      print('c:', i, check_max[i])

print(somefunction(s))
