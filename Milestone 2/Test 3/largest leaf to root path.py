import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def longestPath(root):
    if root is None:
        return []

    left = longestPath(root.left)
    right = longestPath(root.right)

    if len(left)>len(right):
        left.append(root.data)
        return left
    else:
        right.append(root.data)
        return right


    pass


def buildLevelTree(levelorder):
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
path = longestPath(root)
for ele in path:
    print(ele)


# Given a binary tree, return the longest path from leaf to root. Longest means, a path which contain maximum number of nodes from leaf to root.
# Input format :
#
# Elements in level order form (separated by space)
#
# (If any node does not have left or right child, take -1 in its place)
#
# Line 1 : Binary Tree 1 (separated by space)
#
# Sample Input 1 :
#  5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# Sample Output 1 :
# 9
# 3
# 6
# 5