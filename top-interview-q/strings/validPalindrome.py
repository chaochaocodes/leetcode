# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

import re

def isPalindrome(s):
    if s == "" : 
        return True

    lowercaseS = s.lower()
    lettersArray = re.findall('[0-9A-Za-z]', lowercaseS)
    reverseArray = lettersArray[:]
    reverseArray.reverse()

    if lettersArray == reverseArray:
        return True
    else: 
        return False


ss = "A man, a plan, a canal: Panama" # True
s2 = "race a car" # False

isPalindrome(s2)


# 2. Using .isalunum (is alphanumeric)
def isPalindrome(s):
    s_check = (''.join(ch for ch in s if ch.isalnum())).lower()
    if s_check == s_check[::-1]:
        return True
    return False