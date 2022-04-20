from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skipMdeleteN(head, m, n):
    if m == 0 or head is None:
        return None
    if n == 0:
        return head
    l = None
    r = None
    prev = None
    while (True):
        i = 0
        j = 0
        while i < n:
            if prev is  None:
                prev = head
            if i<m:
                prev = prev.next
            if r is None:
                r = head
            else:
                if r.next is None:
                    return head
                r = r.next
            i=i+1
        while (j < m):
            if l is None:
                l = head
                r = r.next
            else:
                l = l.next
                if r.next is None:
                    if i+1>=m:
                        a1= prev.data
                        prev.next = None
                        return head
                r = r.next
            j=j+1

        l.next = r.next
        r=l
        prev = r


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
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1