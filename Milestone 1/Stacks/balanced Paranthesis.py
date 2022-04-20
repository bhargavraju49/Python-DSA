from sys import stdin


def isBalanced(s):
    s1 = []
    for i in s:
        if i == '(':
            s1.append(i)
        if i == ')':
            if not s1:
                return False
            if s1[- 1] == '(':
                s1.pop()
            else:
                return False
    if not s1:
        return True
    else:
        return False


# main
expression = stdin.readline().strip()

if isBalanced(expression):
    print("true")

else:
    print("false")