def sumArray(arr):
    if len(arr)==1:
        return arr[0]
    sum = arr[0] + sumArray(arr[1:])
    return sum
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
