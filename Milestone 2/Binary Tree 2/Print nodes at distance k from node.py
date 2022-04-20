from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
a=[]
def nodesAtDistanceK(root, node, k):
    if root is None:
        return -1
    if root.data == node:
        helpersum(root,k)
        return 1
    l = nodesAtDistanceK(root.left,node,k)
    r = nodesAtDistanceK(root.right,node,k)
    if l!=-1  and l<=k:
        if l==k:
            print(root.data)
        else:
            helpersum(root.right,k-l-1)
        return l+1
    elif r!=-1 and r<=k:
        if r==k:
            print(root.data)
        else:
            helpersum(root.left,k-r-1)
        return r+1
    else:
        return -1
def helpersum(root,d):
    if root is None:
        return
    if d == 0:
        print(root.data)
    helpersum(root.left,d-1)
    helpersum(root.right,d-1)
    return


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])

nodesAtDistanceK(root, target, k)