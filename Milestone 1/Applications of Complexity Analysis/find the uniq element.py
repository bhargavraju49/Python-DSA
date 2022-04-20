from sys import stdin


def findUnique (a ,n):
    # Your code goes here
    a.sort()
    i = 0
    while i < n - 1:
        if a[i] != a[i + 1]:
            if a[i - 1] != a[i]:
                return a[i]

        else:
            i = i + 2
    return a[n - 1]


# taking input using fast I/O method
def takeInput ():
    n = int(stdin.readline().strip())
    if n == 0:
        return list() ,0

    arr = list(map(int ,stdin.readline().strip().split(" ")))
    return arr ,n


def printList (arr ,n):
    for i in range(n):
        print(arr[i] ,end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr ,n = takeInput()
    print(findUnique(arr ,n))

    t -= 1