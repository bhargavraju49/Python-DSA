def firstIndex(arr, x):
    if len(arr) == 1:
        if arr[0] == x:
            return 0
        else:
            return -1
    if arr[0] == x:
        return 0
    k=firstIndex(arr[1:],x)
    index = k+1
    if k<0:
        return -1
    return index
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))
