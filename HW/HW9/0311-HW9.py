class TreeNode:
    def __init__(self, root):
        self.value = root
        self.left = None
        self.right = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root.left == None): return root.value
        # print(root.value)
        # if p and q are smaller than current node, explore left subtree
        if p.value < self.value and q.value < self.value:
            return self.lowestCommonAncestor(root.left, p, q)
        # if p and q are larger than current node, explore right subtree
        elif p.value > self.value and q.value > self.value:
            return self.lowestCommonAncestor(root.right, p, q)
        # if nothing is both smaller and greater, its the lca
        else: return root.value

def main():
    
    root = TreeNode(4)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(9)

    print("LCA: ", root.lowestCommonAncestor(root, root.left.left, root.right.left)) # testcase 1 (p:1 q:5, answer: 4)
    print("LCA: ", root.lowestCommonAncestor(root, root.left, root.left.left)) # testcase 2 (p:3 q:1, answer: 3)

if __name__ == "__main__":
    main()