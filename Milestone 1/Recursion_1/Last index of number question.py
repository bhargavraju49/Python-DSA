def lastIndex (arr ,x):
    if len(arr) == 0:
        return -1
    slist = arr[1:]
    index = lastIndex(slist ,x)
    if index != -1:
        return index + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
n = int(input())
arr = list(int(i) for i in input().strip().split(' '))
x = int(input())
print(lastIndex(arr ,x))