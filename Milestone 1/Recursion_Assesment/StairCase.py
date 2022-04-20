def lad(n):
    if n>0 and n<4:
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 4
    if n>3:
        s = lad(n-1)+ lad(n-2) + lad(n-3)
    return s

n = int(input())
print(lad(n))