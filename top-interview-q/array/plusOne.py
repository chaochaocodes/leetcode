digits1 = [1,2,3] # 123 + 1 => [1,2,4]
digits2 = [1,9,9] # 199 + 1 => [2,0,0]

# loop and increment +1 from end
# carry over case:  if digit[i] = 9, then digit[0], and digit[i-1] +1


# 1. Converting data structures
def plusOne(digits):
  digitStr = ''
  for i in digits:
    digitStr += str(i)

  digitInt = list(str(int(digitStr)+1))
  return digitInt


# 2. Using a carry
def plusOne(digits):

    carry= 1
    for i in range(len(digits)-1, -1, -1):

        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += carry
            carry = 0
            break

    if carry == 1:
        digits.insert(0, carry)

    return digits

