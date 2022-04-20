from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def rev(head,c,k,co):
    sh = c
    a1 = c.data
    head1 = c.next
    i = 0
    c = c.next
    while i < k - 1:
        n = c.next
        a2 = n.data
        if c.next.next is None:
            c.next = None
            n.next = head1
            sh.next = n
            return head
        c.next = c.next.next
        n.next = head1
        head1 = n
        sh.next = head1
        i = i + 1
    return rev(head, c, k ,co-i-1)

def kReverse(head, k):
    if k == 0 or k == 1 or head is None:
        return head
    l = 1
    temp = head
    while (temp.next is not None):
        l = l + 1
        temp = temp.next
    i = 0
    c = head
    while i < k - 1:
        n = c.next
        if c.next.next is None:
            c.next = None
            n.next = head
            return n
        c.next = c.next.next
        n.next = head
        head = n
        i = i + 1
    if l%k!=0 or 2*k == l:
        return rev(head,c,k,(l-i-1))
    else:
        return head


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

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


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1