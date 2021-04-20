'''
Sorting: Bubble Sort

for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }    
}
Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

1. Array is sorted in numSwaps swaps., 
where numSwaps is the number of swaps that took place.
2. First Element: firstElement, 
where  is the first element in the sorted array.
3. Last Element: lastElement, 
where  is the last element in the sorted array.
'''
a = [6,4,1] # 3, 1, 6
b = [3,2,1] # 3, 1, 3
c = [1,2,3] # 0, 1, 3

def countSwaps(a):
    swaps = 0
    for i in range(len(a)): 
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1

    result = 'Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}'.format(swaps, a[0], a[-1])
    print(result)

print(countSwaps(a))

# Multiline prints Tabs when aligned in HackerRank
# result = '''
#         Array is sorted in {} swaps.
#         First Element: {}
#         Last Element: {}
#         '''.format(swaps, a[0], a[-1])