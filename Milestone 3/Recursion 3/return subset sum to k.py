import sys
sys.setrecursionlimit(10 ** 8)


def test(a,k,c):
    if len(a)==0 and k!=0:
        return
    if k==0:
        res.append(c[1:])
        return
    if k<0:
        return

    test(a[1:],k-a[0],c+' '+str(a[0]))
    test(a[1:],k,c)

    pass

#taking input
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi) :
    for li in liOfLi :
        print(li)

#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    res = []
    c = ''
    test(arr, k, c)
    printListOfList(res)