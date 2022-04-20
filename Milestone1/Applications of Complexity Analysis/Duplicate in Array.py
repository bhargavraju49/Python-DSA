from sys import stdin


def findDuplicate(arr, n) :
    arr.sort()
    i=0
    while i<n-1:
        if arr[i]==arr[i+1]:
            return arr[i]
        i=i+1


#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1