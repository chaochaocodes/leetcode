from collections import Counter 

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # store note in dict
    # store magazine in dict
    n, m = Counter(note), Counter(magazine)
    res = ''
    # loop through note_dict, if in mag_dict
    for i in n:
        # check: if word occurs more often in note than magazine
        if i not in m or n[i] > m[i]:
            res ='No'
            break
        else: 
            res = 'Yes'
    # print Yes or No, do not return anything
    print(res)


print(checkMagazine(m, n))

m1 = ['give', 'me', 'one', 'grand', 'today', 'night']
n1 = ['give', 'one', 'grand', 'today']
# Yes
m2 = ['two', 'times', 'three', 'is', 'not', 'four']
n2 = ['two', 'times', 'two', 'is', 'four']
# No
