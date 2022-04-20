from sys import stdin


def pairSum(arr, n, nu):
    # Your code goes here
    arr.sort()
    c = 0
    for j in range (n-2):
        N= nu - arr[j]
        k={}
        for i in range(j+1,n):
            b = N - arr[i]
            if b in k.keys():
                c = c+ k[b]
            if arr[i] not in k.keys():
                k[arr[i]]=1
            else:
                k[arr[i]] = k[arr[i]] +1
    return c

# taking input using fast I/O method
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
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1