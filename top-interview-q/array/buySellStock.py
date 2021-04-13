def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) <= 1:
        return 0
    tot = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            tot += prices[i] - prices[i-1]
    return tot
  


# prices = [7,1,5,3,6,4]
#   if len(prices) <= 1: return 0

#   i, j = 0, 1
#   max_profit = 0
#   while i < len(prices):
#     while j < len(prices):
#       if j>i and j!=i:
#         print('i,j:', i,j)
#         temp = prices[j] - prices[i]
#         print('temp:', temp)

#         max_profit = max(max_profit, temp)
#         print(max_profit)

#   print(max_profit)
#   return max_profit


# maxProfit(arr)
