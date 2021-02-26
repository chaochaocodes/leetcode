def jumpingOnClouds(c, n):
    # c.insert(n,0)
    # count = 0
    # i = 0 
    # while (i < n-1):
    #     i += (c[i+2] == 0) + 1
    #     count += 1
    # print (count)
    pass

def jumpingOnClouds(c, n):
    i = 0
    jumps = 0
    while(i < len(c) - 2):
        if c[i + 2] != 1:
            i +=2
            jumps += 1
        else:
            i +=1
            jumps += 1
    if i == len(c) - 2:
        jumps += 1

    return jumps



c0 = [0, 0, 1, 0, 0, 1, 0]
n0 = 7
c1 = [0, 0, 0, 1, 0, 0]
n1 = 6
print(jumpingOnClouds(c0,n0))   #4
# print(jumpingOnClouds(c1,n1))   #3