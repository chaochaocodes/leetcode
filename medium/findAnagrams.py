# 1. Sliding Window solution
def findAnagrams(string, anagram):
  # sort the anagram and store it back to itself
  anagram = ''.join(sorted(anagram))
  # the current "window"
  window_string = ''
  # result List[int] of start indices
  start_indices = []
  # initialize the start of the window at index 0
  window_start = 0
  # iterate through the entire string, O(n)
  for char in string:
      # slide the right side of the window (equivalent to adding the next character to current string)
      window_string += char
      # start checking the window once the window size is size of anagram
      if len(window_string) == len(anagram):
          # sort the current string in the window and check if it equals the anagram
          if ''.join(sorted(window_string)) == anagram:
              # Anagram found! Append the window start index to start_indices
              start_indices.append(window_start)
          # remove the leftmost character of the window and slide the left side of the window
          window_string = window_string[1:]
          window_start += 1
  return start_indices
  
s = "cbaebabacd"
p = "abc"
# Output: [0,6]
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
findAnagrams(s,p)


# s = "abab"
# p = "ab"
# Output: [0,1,2]



# 2. defaultdict / Counter => exceeds time limit
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         dic = collections.defaultdict(str)
#         psort = "".join(sorted(p))
#         dic[psort] = p
#         n = len(p)

#         result = list()
#         for idx, i in enumerate(s):
#             substr = "".join(sorted(s[idx:idx+n]))
#             if dic[substr]:
#               result.append(idx)
        
#         return result

# 3. Exceeds time limit without hash map 
# # class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         p = "".join(sorted(p))
#         n = len(p)

#         result = list()
#         for idx, i in enumerate(s):
#             if "".join(sorted(s[idx:idx+n])) == p:
#               result.append(idx)
        
#         return result