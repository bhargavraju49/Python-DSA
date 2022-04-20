from sys import stdin


def stockSpan(price, n):
    if n == 1:
        return 1
    s = []
    res = [1]
    s.append(0)
    for i in range(1, n):
        k=price[s[-1]]
        g=price[i]
        while ( s and price[s[-1]] < price[i]):
            s.pop()
        if not s:
            res.append(i + 1)
        else:
            res.append(i - s[-1])
        s.append(i)

    return res


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

    print()


def takeInput():
    size = int(stdin.readline().strip())

    if size == 0:
        return list(), 0

    price = list(map(int, stdin.readline().strip().split(" ")))

    return price, size


# main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)