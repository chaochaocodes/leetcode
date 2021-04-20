'''A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]. 

** Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array 'a' of 'n' integers and a number,'d', perform 'd' left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Input:
int a[n]:  array to rotate
int d: number of rotations

Output:
int a'[n]: rotated array

'''
def rotLeft(a, d):
    a = list(a)
    return a[d:] + a[:d]



# a[0] = 3-0 = 3
# a[1] = 3+1 = 4 
# a[2] = 3+2 = 5
# a[3] = 3-2 = 1 
# a[4] = 3-1 = 2 


print(rotLeft([1,2,3,4,5], 4))
# Output: 5 4 3 2 1
# Output: 3,4,5,1,2     = 2 rotations