from sys import stdin

def checkRedundantBrackets(a) :
    s1=[]
    s='*-+/'
    p='(/*-+'
    k=0
    for i in a:
        if i!=')' and i in p:
            s1.append(i)
        elif i==')':
            c=s1.pop()
            if c in s and k==0:
                k=1
                s1.pop()
            elif c in s and k!=0:
                return False
            elif c == '(':
                return True


#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
    print("true")

else :
    print("false")