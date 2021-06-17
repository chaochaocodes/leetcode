'''
Your job is to sort giraffes into groups based on the lengths of their necks. The giraffes get anxious if their group contains giraffes with much longer necks than theirs. So, you’ll need to make sure that the differences between neck lengths in a group is not greater than 2. The input you get is a one-dimensional array of length N, with lengths between 1 and 20. The desired output is a two-dimensional

organize an array of numbers in such a way that the differences between neighbouring numbers is less than or equal to 2. You need to transform the array of numbers into an array of arrays of numbers, or “groups”.
'''

A = [1, 2, 3, 8, 10, 20]
N = len(A)
B = list()
inner = list()
B.append(inner)
B[0].append(A[0])

i = 0
j = 0
while i < N-1:
  if A[i+1] - B[j][0] <= 2:
    B[j].append(A[i+1])
  else:
    newlist = list()
    B.append(newlist)
    j+= 1
    B[j].append(A[i+1])
  
  i += 1
  print(B)