'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

n = 2 # 2
nn = 3 # 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Approach: Dynamic Programming
def climbStairs(n):
    # base cases
    if n < 2:
        return n    
    # dp table base cases
    dp = [None]*(n+1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]