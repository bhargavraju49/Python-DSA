from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__ (self ,data):
        self.data = data
        self.next = None


def appendLastNToFirst (head ,n):
    if n == 0:
        return head
    if head is None:
        return None
    first = head
    dummy = Node(1)
    dummy.next = first
    second = dummy
    x = 0
    while (x < n - 1):
        first = first.next
        x = x + 1
    while (first.next) is not None:
        second = second.next
        first = first.next

    k = second.next
    second.next = None
    first.next = head
    return k


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


# to print the linked list
def printLinkedList (head):
    while head is not None:
        print(head.data ,end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head ,n)
    printLinkedList(head)

    t -= 1 