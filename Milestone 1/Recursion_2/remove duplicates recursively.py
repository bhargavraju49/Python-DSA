# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(s):
    if len(s) == 0 or len(s) == 1:
        return s
    op = removeConsecutiveDuplicates(s[1:])
    if s[0]==s[1]:
        return '' + op
    else:
        return s[0] + op
    pass

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))