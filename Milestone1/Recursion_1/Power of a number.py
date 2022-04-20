a, b = input().split()
a = int(a)
b = int(b)

def pow(a, b):
    if b==0:
        return 1
    if a==0:
        return 0
    x=pow(a,b-1)
    return a*x
print(pow(a,b))