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
        list.append(root.root)
        if root.right is not None:
            self.readTree(root.right, list)

    def isInOrder(self, list):
            for i in range(1, len(list)):
                if list[i-1] >= list[i]: return False
            return True
    
root_node = Node(1)
root_node.left = Node(2)
root_node.left.left = Node(3)
root_node.left.right = Node(4)
root_node.right = Node(8)
root_node.right.left = Node(5)
root_node.right.right = Node(6)

print(root_node.isValidBST(root_node)) # the second testcase