from sys import stdin ,setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__ (self ,data):
        self.data = data
        self.left = None
        self.right = None


def buildTree (p ,i1 ,n):
    if len(p) == 0:
        return None
    rt = BinaryTreeNode(p[-1])
    i = -1
    if p[-1] not in i1:
        return None
    else:
        i = i1.index(p[-1])

    rt.left = buildTree(p[:i] ,i1[:i] ,i)
    rt.right = buildTree(p[i:-1] ,i1[i + 1:] ,i)
    return rt


'''-------------------------- Utility Functions --------------------------'''


def printLevelWise (root):
    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)

        else:
            print(frontNode.data ,end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)


# Taking level-order input using fast I/O method
def takeInput ():
    n = int(stdin.readline().strip())

    if n == 0:
        return list() ,list() ,0

    postOrder = list(map(int ,stdin.readline().strip().split(" ")))
    inOrder = list(map(int ,stdin.readline().strip().split(" ")))

    return postOrder ,inOrder ,n


# Main
postOrder ,inOrder ,n = takeInput()
root = buildTree(postOrder ,inOrder ,n)
printLevelWise(root)