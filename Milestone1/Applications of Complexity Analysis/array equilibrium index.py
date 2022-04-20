from sys import stdin


def arrayEquilibriumIndex(a, n):
    m = n//2
    ls = 0
    rs = 0
    for i in range(n):
        rs = rs + a[i]
    for i in range(n):
        rs = rs - a[i]
        if i>0:
            ls = ls + a[i-1]
        if ls == rs :
            return i
    return -1

# Taking input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t -= 1