class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)
import queue
def printLevelWiseTree(tree):
    q= queue.Queue()
    if tree== None:
        return None
    q.put(tree)
    while (not(q.empty())):
        current_node = q.get()
        #use join function to print the output in specified format
        print(current_node.data,':', ",".join(str(num) for num in current_node.children),sep='')
        for child in current_node.children:
            #print(child.data,",",end='')
            #current_node.children.append(child)
            q.put(child)
        print()
    return tree
def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)