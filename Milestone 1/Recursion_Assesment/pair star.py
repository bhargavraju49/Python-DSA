def sp(s,i,n):
    if i<n:
        if i<n-1:
            if s[i]==s[i+1]:
                x = s[:i+1] + '*' + s[i+1:]
                return sp(x,i+2,n+1)
            else:
                x = s[:i + 1] + s[i + 1:]
                return sp(x, i + 1, n)
        else:
            x = s[:i+1]+s[i+1:]
            return sp(x,i+1,n)
    else:
        return s

s=input()
print(sp(s,0,len(s)))
