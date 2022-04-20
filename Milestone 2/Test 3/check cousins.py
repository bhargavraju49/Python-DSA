# Given the binary Tree and two nodes say ‘p’ and ‘q’. Determine whether the two nodes are cousins of each other or not. Two nodes are said to be cousins of each other if they are at same level of the Binary Tree and have different parents.
# Do it in O(n).
# Input format :
# Line 1 : Nodes in level order form (separated by space). If any node does not have left or right child, take -1 in its place
# Line 2 : integer value of p
# Line 3 : Integer value of q
# Output format :
# true or false
# Constraints :
# 1 <= N <= 10^5
# Sample Input :
# 5 6 10 2 3 4 -1 -1 -1 -1 9 -1 -1 -1 -1
# 2
# 4
# Sample Output :
# true


from collections import deque

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkCousins(root, x, y):
    level = 0
    parent = None

    q = deque([(root, parent)])

    while q:
        level += 1
        for _ in range(len(q)):
            cur, parent = q.popleft()
            if cur.data == x:
                x = (level, parent)
            if cur.data == y:
                y = (level, parent)

            parent = cur.data

            if cur.left is not None:
                q.append((cur.left, parent))

            if cur.right is not None:
                q.append((cur.right, parent))

    return x[0] == y[0] and x[1] != y[1]


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
p = int(input())
q = int(input())
ans = checkCousins(root, p, q)
if ans is True:
    print('true')
else:
    print('false')