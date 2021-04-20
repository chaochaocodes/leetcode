'''
Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

Example
a = 'cde'
b = 'dcf'

Delete e from a and f from b so that the remaining strings are cd and dc which are anagrams. This takes 2 character deletions.
'''

a1 = 'bcdcc'
b1 = 'abcce'
a2 = 'fcrxzwscanmligyxyvym'
b2 = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'


from collections import Counter

def makeAnagram(a, b):
    a = Counter(a)
    b = Counter(b)
    
    # find letters that appear in both strings
    check = [x for x in a if x in b]

    for i in check:
        # if a letter appears more times in one string, delete least amount of appearances
        find_min = min(a[i], b[i])
        a[i] -= find_min
        b[i] -= find_min
    
    return sum(a.values()) + sum(b.values())