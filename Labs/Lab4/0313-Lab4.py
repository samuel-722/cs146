
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def invertTree(root):

    # need to swap every left branch with its right branch so
    # need to go top down, swapping left with the same position on the right
    # stop if it there are no children
    if (root == None): return root
    invertTree(root.left)
    invertTree(root.right)
    temp_side = root.left
    root.left = root.right
    root.right = temp_side


    return root