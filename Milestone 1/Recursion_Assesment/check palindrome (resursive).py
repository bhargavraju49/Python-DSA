def pal (s,i,j):
    if i<j:
        if s[i]==s[j]:
            return pal(s,i+1,j-1)
        else:
            return 'false'
    if i>=j:
        return 'true'

s = input()
print(pal(s,0,len(s)-1))