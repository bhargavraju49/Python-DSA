
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    def printTree(self):
        def helper(r):
            if r is None:
                return

            if r.left is None and r.right is None:
                print(str(r.data) + ':')
            if r.left is not None and r.right is not None:
                print(str(r.data) + ':' + 'L:' + str(r.left.data) + ',' + 'R:' + str(r.right.data))
            if r.left is not None and r.right is None:
                print(str(r.data) + ':' + 'L:' + str(r.left.data) + ',')
            if r.left is None and r.right is not None:
                print(str(r.data) + ':' + 'R:' + str(r.right.data))
            helper(r.left)
            helper(r.right)

        helper(self.root)

    def search(self, data):
        if self.root is None:
            return False

        def helper(root, x):
            if root is None:
                return
            if x < root.data:
                return helper(root.left, x)
            if x == root.data:
                return True
            if x > root.data:
                return helper(root.right, x)
            return False

        return helper(self.root, data)

    def insert(self, data):
        self.numNodes += 1
        if self.root is None:
            self.root = BinaryTreeNode(data)
            return self.root

        def helper(root):
            if data <= root.data:
                if root.left is None:
                    root.left = BinaryTreeNode(data)
                else:
                    helper(root.left)

            else:
                if root.right is None:
                    root.right = BinaryTreeNode(data)
                else:
                    helper(root.right)

        helper(self.root)

    def deleteHelper(self, root, data):
        if root is None:
            return False, None
        if root.data > data:
            deleted, newLeft = self.deleteHelper(root.left, data)
            root.left = newLeft
            return deleted, root
        if root.data < data:
            deleted, newRight = self.deleteHelper(root.right, data)
            root.right = newRight
            return deleted, root
        if root.left == None and root.right == None:
            return True, None
        if root.right == None:
            return True, root.left
        if root.left == None:
            return True, root.right

        min = self.minVal(root.right)
        root.data = min
        deleted, newRight = self.deleteHelper(root.right, min)
        root.right = newRight
        return True, root

    def delete(self, data):
        deleted, newRoot = self.deleteHelper(self.root, data)
        if deleted:
            self.numNodes -= 1
        self.root = newRoot
        return deleted

    def count(self):
        return self.numNodes

    def minVal(self, root):
        if root.left is None:
            return root.data
        return self.minVal(root.left)


b = BST()
q = int(input())
while (q > 0):
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q -= 1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()