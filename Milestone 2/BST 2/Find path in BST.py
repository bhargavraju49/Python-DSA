import queue


class BinaryTreeNode:
    def __init__ (self ,data):
        self.data = data
        self.left = None
        self.right = None


def findPathBST (root ,data):
    if root is None:
        return None
    if root.data == data:
        l = list()
        l.append(data)
        return l
    left = findPathBST(root.left ,data)
    right = findPathBST(root.right ,data)
    if left is not None:
        left.append(root.data)
        return left
    elif right is not None:
        right.append(root.data)
        return right
    else:
        return None


def buildLevelTree (levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root


# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
data = int(input())
path = findPathBST(root ,data)
if path is not None:
    for ele in path:
        print(ele ,end=' ')