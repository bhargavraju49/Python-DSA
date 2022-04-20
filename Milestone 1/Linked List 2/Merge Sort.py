from sys import stdin ,setrecursionlimit

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__ (self ,data):
        self.data = data
        self.next = None


def mergeTwoSortedLinkedLists (h1 ,h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1
    p1 = h1
    p2 = h2
    prev = None
    while (p1 is not None and p2 is not None):
        if p1.data < p2.data:
            prev = p1
            p1 = p1.next
        else:
            if prev is not None:
                prev.next = p2
            prev = p2
            p2 = p2.next
            prev.next = p1
    if p1 is None:
        prev.next = p2
    if h1.data < h2.data:
        return h1
    else:
        return h2


def mergeSort (head):
    if head is None or head.next is None:
        return head

    fast = head
    slow = head
    while (fast.next is not None and fast.next.next is not None):
        fast = fast.next.next
        slow = slow.next
    head2 = slow.next
    slow.next = None
    p1 = mergeSort(head)
    p2 = mergeSort(head2)
    sl = mergeTwoSortedLinkedLists(p1 ,p2)
    # printLinkedList(p2)

    return sl


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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1