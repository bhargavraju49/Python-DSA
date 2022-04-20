# Problem: Remove x from string
def removeX(string):
    if len(string)==0:
        return ''
    op = removeX(string[1:])
    if string[0] == 'x':
        return ''+op
    else:
        return string[0]+op
    return op
    pass

# Main
string = input()
print(removeX(string))