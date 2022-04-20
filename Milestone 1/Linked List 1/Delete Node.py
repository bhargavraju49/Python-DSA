from sys import stdin


# Following is the Node class already written for the Linked List.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    curr = head
    c = 0
    while(curr!=None):
        curr = curr.next
        c = c + 1
    return c

def deleteNode(head, pos):
    c = head
    i = 0
    l = length(head)
    if pos>l and pos>0:
        return head
    if pos == 0 and l<1:
        return None
    if pos == 0 and l>1:
        return head.next
    else:
        while(i<pos-1):
            c = c.next
            i = i +1
        if l!=pos:
            c.next = c.next.next
            return head
        else:
            c.next=None
            return head

# Taking Input Using Fast I/O.
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


# To print the linked list.
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()
    pos = int(stdin.readline().rstrip())

    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1