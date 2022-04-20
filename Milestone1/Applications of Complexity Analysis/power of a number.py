def power(x, n):
    # Please add your code here
    if n==0 or n==1:
        return 1
    else:
        s = x*power(x,n-1)
        if n == 0:
            return s*s
        elif n == 1:
            return s*s*x
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))