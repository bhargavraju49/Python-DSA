from sys import stdin


def pairSum(arr, n, num):
    # Your code goes here
    arr.sort()
    i = 0
    j = n - 1
    c = 0
    while i < j:
        if arr[i] == arr[j] and arr[i] + arr[j] == num:
            return c + ((j - i + 1) * (j - i)) // 2
        if arr[i] + arr[j] == num:
            a = arr[i]
            b = arr[j]
            a1 = 0
            b1 = 0
            while arr[i] == a:
                i = i + 1
                a1 = a1 + 1
            while arr[j] == b:
                j = j - 1
                b1 = b1 + 1
            c = c + a1*b1

        elif arr[i] + arr[j] < num:
            i = i + 1
        elif arr[i] + arr[j] > num:
            j = j - 1
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