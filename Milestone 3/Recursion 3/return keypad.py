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

def subsequences(s):
    if len(s) == 1:
        output = keys(int(s))
        return output
    smallerString = s[1:]
    smallerOutput = subsequences(smallerString)

    output = []
    skeys = keys(int(s[0]))

    for sub in smallerOutput:
        for ki in skeys:
            subs_with_zeroth_char = ki + sub
            output.append(subs_with_zeroth_char)

    return output


string = input()
#keys= [[''],[''],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
ans = subsequences(string)
for ele in ans:
    print(ele)