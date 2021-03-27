def isPowerOfThree(n):
    if n < 3:
        return False
    while n%3 == 0:
        n /= 3
    return n == 1

# 1 is a power of 3