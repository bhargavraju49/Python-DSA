def cnt(n):
    if n>0 and n<9:
        return 0
    if n == 0:
        return 1
    if n%10 == 0:
        return 1+cnt(n//10)
    else:
        return cnt(n//10)

print(cnt(int(input())))