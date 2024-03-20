from typing import List, Optional

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        current = [root]

        while current:
            next_level = []
            values = []

            for node in current:
                values.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)

            result.append(values)
            current = next_level
        return result
    

root = TreeNode(4)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.right = TreeNode(8)
root.right.left = TreeNode(5)
root.right.right = TreeNode(9)

print(root.levelOrder(root)) #testcase