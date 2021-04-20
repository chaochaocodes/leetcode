# Find number of a's in first n letters of s
s = 'aba' # repeats infinitely
n = 10 # min length of substring

import math
from collections import Counter

# Approach 5:  use .count() with Approach #4 logic
def repeatedString(s, n):
  return s.count('a') * (n // len(s)) + s[:n % len(s)].count("a")

print(repeatedString(s,n))


# Approach 1: List (Brute force)
def repeatedString(s, n):
    # find substring
    lenS = len(s)
    lenSub = lenS
    substring = s
    while n > lenSub:
        substring = substring + s
        lenSub = lenSub + lenS
    
    count = 0
    # Count substring up till n letters
    for i in range(n):
        if substring[i] == 'a':
        count += 1
    return count

# Approach 2: Dictionary
def repeatedString(s, n):
    # find substring
    lenS = len(s)
    lenSub = lenS
    substring = s
    while n > lenSub:
        substring = substring + s
        lenSub = lenSub + lenS
        
    count_a = dict()
    for i in range(n):
        if substring[i] == 'a':
        count_a['a'] = count_a.get('a', 0) + 1
    return count_a['a']

# Approach 3: Counter
def repeatedString(s, n):
    # edge case
    if len(s) == 1:
        return n
    # find substring
    repeat = math.ceil(n / len(s))
    substring = s * repeat
    # count substring up till n letters
    substring = substring[:n]
    count_a = Counter(substring)
    return count_a['a']

# Approach 4: Create counter first! Avoid potential giant substring
def repeatedString(s, n):
    # initiate counter from s, then multiply counter values
    counter_s = Counter(s)
    repeat = round(n/len(s))
    dict_comp = {k:(v*repeat) for (k,v) in counter_s.items()}
    # find remaining substring up till n, slice s up to remainder 
    remainder = s[: n % len(s) ]
    # update Counter
    for i in remainder:
        dict_comp[i] = dict_comp.get(i, 0) + 1

    return (dict_comp['a'])