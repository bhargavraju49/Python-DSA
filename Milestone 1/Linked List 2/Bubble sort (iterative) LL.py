from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def bubbleSort(head) :
    if head is None or head.next is None:
        return None
    sum=1
    l=0
    prev = None
    temp = head
    while(temp is not None):
        l=l+1
        temp=temp.next
    c = head
    prev= None
    while True:
        prev = None
        c=head
        k = 0
        for i in range(l-1):
            if c.data > c.next.data:
                if prev is None:
                    n=c.next
                    c.next = c.next.next
                    n.next = c
                    prev=n
                    head = prev
                else:
                    n=c.next
                    c.next = c.next.next
                    n.next = c
                    prev.next=n
                    prev = n
                k = k+1
            else:
                c=c.next
                if prev is None:
                    prev = head
                else:
                    prev=prev.next
        if k == 0:
            break
    return head


def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)