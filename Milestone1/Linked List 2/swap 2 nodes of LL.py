from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__ (self ,data):
        self.data = data
        self.next = None


def swapNodes (head ,i ,j):
    p1 = None
    c1 = head
    m = 0
    while (m < i):
        if p1 is None:
            p1 = head
            c1 = head.next
        else:
            p1 = p1.next
            c1 = c1.next
        m = m + 1
    n1 = c1.next
    if i + 1 == j:
        c1.next = c1.next.next
        p1.next = n1
        n1.next = c1
        return head
    p2 = None
    c2 = head
    m1 = 0

    while (m1 < j):
        if p2 is None:
            p2 = head
            c2 = head.next
        else:
            if c2.next is not None:
                p2 = p2.next
                c2 = c2.next
        m1 = m1 + 1
    if c2.next is None:
        p1.next = c2
        c2.next = n1
        p2.next = c1
        c1.next = None
    else:
        n2 = c2.next
        p1.next = c2
        c2.next = n1
        p2.next = c1
        c1.next = n2
    return head


# Taking Input Using Fast I/O
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


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head ,i ,j)
    printLinkedList(newHead)

    t -= 1