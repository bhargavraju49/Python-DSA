from sys import stdin


def pairSum0(l, n):
    k=dict()
    for i in l:
        k[i] = k.get(i,0)+1
    s=0
    #print(k)
    for i in k:
        if i==0:
            x=k[i]
            s+=(x*(x-1))
        elif k.get(-i)!=None:
            s+=k.get(i)*k.get(-i)
    return s//2


def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


arr, n = takeInput()
print(pairSum0(arr, n))