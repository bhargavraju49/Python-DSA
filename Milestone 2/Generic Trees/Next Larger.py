from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def nextLargest(tree, n):
    q=queue.Queue()
    q.put(tree)
    max = 0
    node = None
    while (not(q.empty())):
        k = q.get()
        for i in k.children:
            q.put(i)
        if int(k.data) > n and max == 0:
            max = int(k.data)
            node=k
        if k.data>n and k.data<max:
            max = int(k.data)
            node=k
    return node

    pass


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
arr = list(int(x) for x in stdin.readline().strip().split())
n = int(input())
tree = createLevelWiseTree(arr)
if nextLargest(tree, n):
    print(nextLargest(tree, n).data)