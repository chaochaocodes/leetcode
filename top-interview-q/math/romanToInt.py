class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        result = 0
        prev_value = 0
        for letter in s:
            value = roman_to_int[letter]
            result += value
            if value > prev_value:
                # if the preceding roman nummber is smaller
                # we need to undo the previous addition
                # and substract the preceding roman char
                # from the current one, i.e. we need to
                # substract twice the previous roman char
                result -= 2 * prev_value
            prev_value = value
        return result

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        n = len(s)
        res = 0
        for i in range(n):
            if  i==n-1 or roman[s[i]] >= roman[s[i+1]]:
                # if following number is smaller or equal, add current number
                res += roman[s[i]]
            else :
                # if following number is greater, subtract current number
                res -= roman[s[i]]
                
        return res