def minimumBribes(q):
    bribes = 0
    # adjust index to be intuitive, now value of p == it's index
    q = [p-1 for p in q]
    for i, p in enumerate(q):
        # i = curr position, p = original position
        # check if if curr > 2 ahead of original position
        if p - i > 2:
            print('Too chaotic')
            return 
            # From here on out, we don't care if P has moved
            # forwards, it is better to count how many times
            # P has RECEIVED a bribe, by looking at who is
            # ahead of P.  P's original position is the value
            # of P.
            # Anyone who bribed P cannot get to higher than
            # one position in front if P's original position,
            # so we need to look from one position in front
            # of P's original position to one in front of P's
            # current position, and see how many of those 
            # positions in Q contain a number large than P.
            # In other words we will look from P-1 to i-1,
            # which in Python is range(P-1,i-1+1), or simply
            # range(P-1,i).  To make sure we don't try an
            # index less than zero, replace P-1 with
            # max(P-1,0)
        for j in range(max(p-1, 0), i):
            if q[j] > p:
                bribes += 1
                
    print(bribes)


q1 = [2, 1, 5, 3, 4]  # 3
q2 = [2, 5, 1, 3, 4]  # Too chaotic!
q3 = [5, 1, 2, 3, 7, 8, 6, 4] # Too chaotic
q4 = [1, 2, 5, 3, 7, 8, 6, 4] #7

print(minimumBribes(q4))

# q4 = [1, 2, 3, 4, 5, 6, 7, 8] #7
# # 5 bribed 2 people: 
# q4 = [1, 2, 5, 3, 4, 6, 7, 8] #7
# # 7 bribed 2 people:
# q4 = [1, 2, 5, 3, 7, 4, 6, 8] #7
# # 8 bribed 2 people: 
# q4 = [1, 2, 5, 3, 7, 8, 4, 6] #7
# # 6 bribed 1 person:
# q4 = [1, 2, 5, 3, 7, 8, 6, 4] #7
