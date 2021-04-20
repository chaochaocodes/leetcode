'''
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Example:
s = mom
anagrammatic pairs: 2 -- [m,m], [mo, om]
'''
s0 = 'mom'
s1 = 'ifailuhkqq' # 3
s2 = 'kkkk' # 10

# Approach 1:  
def sherlockAndAnagrams(s):
    anagram_dict = {}
    count = 0
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            current_sorted = str(sorted(s[j:j+i]))
            print(current_sorted)
            if (current_sorted not in anagram_dict):
                anagram_dict[current_sorted] = 1
            else:
                count += anagram_dict[current_sorted]
                anagram_dict[current_sorted] += 1
            print(anagram_dict)
            print(count)
    return count

# Approach 2
# def sherlockAndAnagrams(s):
#     count=0
#     for slice_len in range(1,(len(s))):
#         mix=[]
#         for i in range(len(s)-slice_len+1):
#             mix.append(s[i:i+slice_len])
#         for j in range(len(mix)):
#             for k in range(j+1,len(mix)):
#                 if sorted(mix[j])==sorted(mix[k]):
#                     count+=1
#     return count


print(sherlockAndAnagrams(s2))