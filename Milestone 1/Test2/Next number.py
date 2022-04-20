## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__ (self ,data):
        self.data = data
        self.next = None


def carry (head):
    if head is None:
        return 1
    res = head.data + carry(head.next)
    head.data = res % 10
    return res // 10


def nextNumber (head):
    k = carry(head)
    if k:
        k = Node(k)
        k.next = head
        return k
    return head


def ll (arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll (head):
    while head is not None:
        print(head.data ,end=' ')
        head = head.next
    return


# Main
# Read the link list elements including -1
arr = [int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)


# Next Number
# Send Feedback
# Given a large number represented in the form of a linked list. Write code to increment the number by 1 in-place(i.e. without using extra space).
# Note: You don't need to print the elements, just update the elements and return the head of updated LL.
# Input Constraints:
# 1 <= Length of Linked List <=10^6.
# Input format :
# Line 1 : Linked list elements (separated by space and terminated by -1)
# Output Format :
# Line 1: Updated linked list elements
# Sample Input 1 :
# 3 9 2 5 -1
# Sample Output 1 :
# 3 9 2 6
# Sample Input 2 :
# 9 9 9 -1
# Sample Output 1 :
# 1 0 0 0


