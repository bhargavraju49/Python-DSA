from sys import stdin ,setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__ (self ,data):
        self.data = data
        self.left = None
        self.right = None


def printLevelWise (root):
    if root is None:
        return root
    q = queue.Queue()
    q.put(root)
    while (q.qsize() != 0):
        k = q.get()
        if k.left is None:
            l = -1
        else:
            l = k.left.data
            q.put(k.left)

        if k.right is None:
            r = -1
        else:
            r = k.right.data
            q.put(k.right)
        print(str(k.data) + ':L:' + str(l) + ',R:' + str(r))


# Taking level-order input using fast I/O method
def takeInput ():
    levelOrder = list(map(int ,stdin.readline().strip().split(" ")))
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


# Main
root = takeInput()
printLevelWise(root)