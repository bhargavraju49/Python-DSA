from sys import stdin


class Node:
    def __init__ (self ,data):
        self.data = data
        self.next = None


def midPoint (head):
    if head is None or head.next is None:
        return head
    fst = head
    slw = head
    while (fst.next is not None):
        if fst.next.next is None:
            return slw
        fst = fst.next.next
        slw = slw.next
    return slw
    pass


def takeInput ():
    head = None
    tail = None

    datas = list(map(int ,stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList (head):
    while head is not None:
        print(head.data ,end=" ")
        head = head.next

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()
    mid = midPoint(head)

    if mid is not None:
        print(mid.data)

    t -= 1