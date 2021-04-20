'''
Sorting 

Given a list of toy prices and an amount to spend, 
determine the maximum number of gifts you can buy.

- Each toy can only be purchased once.
'''
prices1, k1 = [1,2,3,4], 7 # 3 items
prices2, k2 = [1, 12, 5, 111, 200, 1000, 10], 50 # 4 items
def maximumToys(prices, k):
    # loop through prices
    # sum of toys < k 
    # maximize by sorting? 
    count = 0
    total = 0
    prices = sorted(prices)
    print(prices)

    for i in prices: 
        if total + i < k:
            total += i
            count += 1

    return count


print(maximumToys(prices1, k1))