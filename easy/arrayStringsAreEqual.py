'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
'''

word1 = ["a", "cb"]
word2 = ["ab", "c"]
# acb != abc, return false

# Approach 1:  Loop over array
# Time: O(n)
def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    
    wordOne = ''
    for i in word1:
        wordOne += i
    
    wordTwo = ''
    for i in word2:
        wordTwo += i
    
    return wordOne == wordTwo

# Approach 2: join()
# Time: O(n)
def arrayStringsAreEqual(word1, word2):
    return "".join(word1) == "".join(word2)
