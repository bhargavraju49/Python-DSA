def checkNumber(arr, x):
    if len(arr)==1:
        if arr[0]==x:
            return True
        else:
            return False
    if arr[0] == x:
        return True
    else:
        return checkNumber(arr[1:],x)
    return False
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
