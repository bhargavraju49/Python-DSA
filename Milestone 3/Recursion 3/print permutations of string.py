def comb(c,k):
    if c=='':
        print(k)
        return
    for i in range(len(c)):
        c=c[1:]+c[0]
        comb(c[1:],k+c[0])
s=input()
comb(s,'')


