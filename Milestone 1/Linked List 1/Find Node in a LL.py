# Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    if head is None:
        return -1
    if head.data == n:
        return 0
    sum =findNode(head.next,n)
    if sum!=-1:
    	return 1 + sum
    else:
        return -1