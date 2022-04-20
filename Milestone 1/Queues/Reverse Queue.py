from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


def reverseQueue(q):
    k = q.qsize()
    if k == 0:
        return -1
    p = q.get()
    reverseQueue(q)
    q.put(p)
    return q



def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n):
        qu.put(values[i])

    return qu


# main
t = int(stdin.readline().strip())

while t > 0:

    qu = takeInput()
    reverseQueue(qu)

    while not qu.empty():
        print(qu.get(), end=" ")

    print()

    t -= 1