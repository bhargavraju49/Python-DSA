from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__ (self ,data):
        self.data = data
        self.next = None


def evenAfterOdd (head):
    newhead = head
    smallhead = None
    if head is None or head.next is None:
        return head
    while (newhead is not None):
        if newhead.data % 2 == 1:
            smallhead = newhead
            break
        newhead = newhead.next
    o = None
    e = None
    prev = None
    n = head
    while (n is not None):
        if n.data % 2 == 1 and e is None:
            o = n
            prev = n
            n = n.next
        elif e is None and n.data % 2 == 0:
            e = n
            prev = n
            n = n.next
        else:
            if e is None:
                return head
            s1 = prev.data
            s2 = n.data
            if prev.data % 2 == 0 and n.data % 2 == 1:
                t = prev.next.next

                if o is None:
                    n.next = e
                    prev.next = t
                    o = n
                    n = t

                else:
                    o.next = n
                    n.next = e
                    o = n
                    prev.next = t
                    n = t

            else:
                prev = prev.next
                n = n.next
    if smallhead is None:
        return head
    else:
        return smallhead


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
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)

    t -= 1