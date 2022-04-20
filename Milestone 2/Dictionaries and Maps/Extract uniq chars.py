def uniqueChar(s):
    k=''
    a=[]
    for i in s:
        if i not in a:
            k+=i
            a.append(i)
    return k
    pass

# Main
s=input()
print(uniqueChar(s))