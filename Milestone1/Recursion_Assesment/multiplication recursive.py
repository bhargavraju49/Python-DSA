def mul(x, y):
    if x<y:
        return mul(y , x)

    elif y!=0:
        return (x + mul(x , y-1))
    else:
        return 0

m = int(input())
n = int(input())
print(mul(m,n))