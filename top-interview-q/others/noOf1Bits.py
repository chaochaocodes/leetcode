'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
'''
n1 = '00000000000000000000000000001011' #3
n2 = '00000000000000000000000010000000' #1
n3 = '11111111111111111111111111111101' #31 '1' bits

'''
Approach 1:  Loop and Flip
Check each of the 32 bits of the number. If bit = 1, add 1 to the number of 1-bits.

Check ith bit using a bit mask, with m = 1 because the binary representation of 1 is 
00000000000000000000000000000001. A logical AND between any number and the mask 1 gives us the least significant bit of this number. To check the next bit, shift mask to the left by one: 00000000000000000000000000000010

Complexity:
Time: O(1) because n in this code is a 32-bit integer
** The Run time depends on the number of bits in n. 
Space: O(1), since no additional space is allocated.
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        mask = 1
        i = 0
        
        while i < 32:
            if (n&mask) != 0:
                bits += 1
            mask <<= 1
            i += 1
        
        return bits


'''
# Approach 2:  Bit Manipulation Trick
Instead of checking every bit of the number, we repeatedly flip the least-significant 1-bit of the number to 0, and add 1 to the sum. As soon as the number becomes 0, we know that it does not have any more 1-bits, and we return the sum.

Trick: realize that for any number n, doing a bit-wise AND of n and n-1 flips the least-significant 1-bit in n to 0. Why? Consider the binary representations of n and n-1.

In the binary representation, the least significant 1-bit in n always corresponds to a 0-bit in n−1. Therefore, adding the two numbers n and n−1 always flips the least significant 1-bit in n to 0, and keeps all other bits the same.

Complexity 
Time: For a 32-bit integer, the run time is O(1)
**The run time depends on the number of 1-bits in n. Worst case, all bits in n are 1-bits. 
Space: O(1), since no additional space is allocated.
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n != 0:
            sum += 1
            n &= (n-1)
        
        return sum

# Python way
class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n:
            sum += n % 2
            n = n >> 1
        
        return sum