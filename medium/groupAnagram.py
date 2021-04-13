import collections

# 1. Solution with Counter
def groupAnagrams(s):
  # build hash map
  # if hash map matches, add to group
  # else create new group

  result = list()     # output list of lists
  dict_group = dict() # dict of dicts
  j = 0               # group no. (dict keys)
  
  for i in s:
    count = collections.Counter(i)
    if count not in dict_group.values():
      dict_group[j] = count         # add to dict
      result.append(list())         # add new list (group)
      result[j].append("".join(i))  # add to result
      j += 1
    else:
      # find find matching key, position = key[value], append result[key]
      position = list(dict_group.keys())[list(dict_group.values()).index(count)]
      result[position].append("".join(i))

# strs = ["a"]
# strs = [""]
# strs = ["eat","tea","tan","ate","nat","bat"]
# [["bat"],["nat","tan"],["ate","eat","tea"]]
groupAnagrams(strs)


# 2. Solution using default dict
# parameter "list" in defaultdict is lowercase
# sorted() returns iterable. We need to join the returned list to create a string
# We can loop through dictionary to store the values in result list or we can directly use dic.values()
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	dic = collections.defaultdict(list)
	for st in strs:
        # sort to compare if anagram
		s = ''.join(sorted(st))
        # unique keys stored in dic, st added to list of values
		dic[s].append(st)

	return dic.values()