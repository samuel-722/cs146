class Node:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

def isValidBST(self, root):
        

def search_binary(self, root, key):
        
    # left nodes only contain nodes less than right nodes
    if root is None or root.value == key:
        return root
    if root.value > key:
            search_binary(root.right, key)