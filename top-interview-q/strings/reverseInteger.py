# // Given a 32-bit signed integer, reverse digits of an integer.
# // Note: Assume we are dealing with an environment which could only store 
# // integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# // Assume that your function returns 0 when the reversed integer overflows.

def reverse(self, x: int) -> int:
    minLimit = -2**31
    maxLimit = 2**31

    strNum = str(x) # Convert x from int to str
    strNum = strNum[::-1] # Reverse digits

    if strNum.endswith("-"):
        strNum = "-" + strNum[:-1] #Remove "-" sign from the end and add it to the beginning

    number = int(strNum)

    if number not in range(minLimit,maxLimit): #Overflow
        return 0

    return number

x1 = 123    # 321
x2 = -123   # -321
x3 = 120    # 21
x4 = 0      # 0

reverse(x2)