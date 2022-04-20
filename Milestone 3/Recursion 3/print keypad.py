def keys(d):
    if d==2:
        return "abc"
    if d==3:
        return "def"
    if d==4:
        return "ghi"
    if d==5:
        return "jkl"
    if d==6:
        return "mno"
    if d==7:
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
    return ""

def subsequences(s,o=''):
    if s==0:
        print(o)
        return
    ld=s%10
    n=s//10
    k = keys(ld)

    for i in k:
        subsequences(n,i+o)

    return





string = int(input())
#keys= [[''],[''],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
subsequences(string)