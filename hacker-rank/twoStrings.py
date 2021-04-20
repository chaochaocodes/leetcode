s1 = "hello"
s2 = "world"
ss1 = "hi"
ss2 = "world"

# check if string1 and string2 share a common substring
# return 'YES' or 'NO' if any letters are shared
from collections import Counter

# Approach 1:  Brute force
def twoStrings(s1, s2):
    s1 = Counter(s1)
    s2 = Counter(s2)

    res = []
    # for any( # if i in n  and i in m)
    for i in s1:
        if i in s2:
            res.append(1)
        else: 
            res.append(0)

    if any(res) == True:
        return "YES"
    else:
        return 'NO'

# Approach 2:  List comprehension
def twoStrings(s1, s2):
    s1 = Counter(s1)
    s2 = Counter(s2)

    res = any([x for x in s1 if x in s2])

    if res == True:
        return "YES"
    else:
        return 'NO'

print(twoStrings(ss1,ss2))
