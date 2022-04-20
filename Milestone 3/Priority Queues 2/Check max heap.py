def checkMaxHeap(lst):
    k=len(lst)
    i = 0
    while 2*i+1 <k:
        p = i
        l = 2*i+1
        r = 2*i+2
        if lst[p] < lst[l]:
            return False
        if r<k and lst[p] < lst[r]:
            return  False
        i = i+1
    return True
    pass


# Main Code
n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')