def subset (a,n,c):
    N=len(a)
    if n==N:
        return
    print(*c)

    for i in range(n+1,N):
        c+=[a[i]]
        subset(a,i,c)
        del c[-1]
    return

n=input()
a=input().split(' ')
if a[-1]=='':
    a=a[:-1]

subset(a,-1,[])