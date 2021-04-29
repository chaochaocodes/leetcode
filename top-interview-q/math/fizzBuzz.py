# Complexity Analysis for all 3 approaches: 
# Time Complexity : O(N)
# Space Complexity : O(1)

# # Approach 1: Naive Approach
# def fizzBuzz(n):
#     """
#     :type n: int
#     :rtype: List[str]
#     """
#     if n < 1: 
#         return []
        
#     result = list()
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             result.append('FizzBuzz')
#         elif i % 3 == 0:
#             result.append('Fizz')
#         elif i % 5 == 0:
#             result.append('Buzz')
#         else: 
#             result.append(str(i))
    
#     print(result)


# # Approach 2: String Concatenation
# def fizzBuzz(n):

#     ans = []

#     for i in range(1, n+1):
#         ans_str = ""
#         if i%3 == 0:
#             ans_str += "Fizz"
#         if i%5 == 0:
#             ans_str += "Buzz"
#         if not ans_str:
#             # not divisible by 3 or 5
#             ans_str = str(i)
            
#         ans.append(ans_str)
#      print(ans)

# fizzBuzz(15)


# Approach 3: Hash table
def fizzBuzz(n):
    ans = []
    d = {3: 'Fizz', 5: 'Buzz'}

    for num in range(1, n+1):
        ans_str = ""

        for key in d.keys():
            if num % key == 0:
                ans_str += d[key]

        if not ans_str:
            ans_str = str(num)

        ans.append(ans_str)
    print(ans)




fizzBuzz(15)