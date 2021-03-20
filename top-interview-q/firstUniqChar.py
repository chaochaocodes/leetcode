def firstUniqChar(s):
    for i in range(len(s)):
        if s.index(s[i]) == s.rindex(s[i]):
            return i
            
    return -1