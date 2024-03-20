package Labs.Lab4;

public class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    public TreeNode invertTree (TreeNode root) {

        if (root == null) return null;
        TreeNode invertLeft = invertTree(root.left);
        TreeNode invertRight = invertTree(root.right);
        TreeNode temp = root.left;
        root.left = invertLeft;
        root.right = invertRight;
        return root;
    }//invert Tree
}//treenode