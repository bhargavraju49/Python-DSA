from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printNodesWithoutSibling(root):
    k=''
    if root is None:
        return ''
    if (root.left is None and root.right is not None):
        k=str(root.right.data)+' '
        #print(root.right.data, end=' ')
    if (root.right is None and root.left is not None):
        #print(root.left.data, end = ' ')
        k=str(root.left.data)+' '
    l = printNodesWithoutSibling(root.left)
    r = printNodesWithoutSibling(root.right)
    return k+l+r


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


# Main
root = takeInput()
print(printNodesWithoutSibling(root))