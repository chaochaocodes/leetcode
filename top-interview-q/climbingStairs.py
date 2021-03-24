# Dyanmic Programming way
# Have dp[i] store the # of different ways to reach step n. 
# The key is the dp[i]relationship, dp[i] = dp[i - 1] + dp[i - 2]

# dp[0] <-- default to 1)
# dp[1] = 1 <-- Only 1 way
# dp[2] = 2 <-- take 2 (1) step OR take 1 (2) step
# dp[3] = 3 <-- take 1 (2) step + 1 (1) step OR 1(1) step + 1(2) step OR 3(1) step
# ...
# dp[3] = dp[2] + d[1] = 2 + 1 = 3

class Solution:
    def climbStairs(self, n):
        dp = [1, 1]
        for i in range(2, n + 1):
            dp.insert(i, dp[i - 1] + dp[i - 2])
        return dp[n]

# Calculating fibonacci(n) way
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        prev = 1
        curr = 2
        for i in range(2,n):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr