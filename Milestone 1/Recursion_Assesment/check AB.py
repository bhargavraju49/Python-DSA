def cs(s):
    if(len(s))>3:
        if s[0]=='a':
            if s[1]=='a':
                return cs(s[1:])
            if s[1]=='b' and s[2] == 'b':
                return cs(s[3:])
            else:
                return 'false'
        else:
            return 'false'
    elif s=='a' or s == 'aa' or s=='aaa' or s=='abb' :
            return 'true'
    else:
        return 'false'

f = cs(input())
print(f)