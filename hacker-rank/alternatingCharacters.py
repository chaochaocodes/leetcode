'''
You are given a string containing characters  and  only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.
'''

def alternatingCharacters(s0):
  # loop through string
  # set pointer? 
  n = len(s0)
  s0 = list(s0)
  pointer = s0[0]
  print(pointer)

  count = 0
  for i in range(1, n):
    if s0[i] != pointer:
      pointer = s0[i]
    else: 
      count += 1

  print(count)    


s0 = 'AAAA' #3
s1 = 'BBBBB' #4
s2 = 'ABABABAB' #0
s3 = 'BABABA' #0
s4 = 'AAABBB' #4

print(alternatingCharacters(s4))