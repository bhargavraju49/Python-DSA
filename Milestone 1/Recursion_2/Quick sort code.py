def qs (a, s, e):
    if s<e:
        p = part(a, s, e)
        qs(a, s, p - 1)
        qs(a, p + 1, e)
    pass
def part (a, s, e):
    if s<e:
        p = a[s]
        c = 0
        for i in range(s,e+1):
            if a[i] < p:
                c = c + 1
        a[s] = a[s+c]
        a[s+c] = p
        pi = s+c
        i=s
        j=e
        while i<j:
            if a[i]<p:
                i=i+1
            elif a[j]>=p:
                j=j-1
            else:
                a[i],a[j] = a[j],a[i]
                i=i+1
                j=j-1
        return pi

n = int(input())
a = list(int(i) for i in input().strip().split(' '))
qs(a, 0, n-1)
print(*a)