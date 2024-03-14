class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
def isValidBST(self, root):
    if root is None:
        return True
    list = []
    self.readTree(root, list)
    return self.isInOrder(list)

def readTree(self, root, list):
    if root.left is not None:
        self.readTree(root.left, list)
    list.append(root.val)
    if root.right is not None:
        self.readTree(root.right, list)