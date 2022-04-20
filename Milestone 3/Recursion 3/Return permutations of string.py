def comb(c,k):
    if c=='':
        ans.append(k)
        return
    for i in range(len(c)):
        c=c[1:]+c[0]
        comb(c[1:],k+c[0])
string = input()
ans = []
comb(string,'')
for s in ans:
    print(s)