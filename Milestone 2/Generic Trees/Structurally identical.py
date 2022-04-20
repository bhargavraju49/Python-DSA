from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
import queue


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def isIdentical(t1, t2):
    x = len(t1.children)
    y = len(t2.children)
    if t1.data!=t2.data:
        return False

    if x==y:
        for i in range (x):
            a1=t1.children[i]
            a2=t2.children[i]
            return isIdentical(a1,a2)

    else:
        return False

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main
arr1 = list(int(x) for x in stdin.readline().strip().split())
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in stdin.readline().strip().split())
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2) is None:
    print('true')
else:
    print('false')