def sm(n):
    if n<9:
        return n
    return n%10+sm(n//10)



print(sm(int(input())))