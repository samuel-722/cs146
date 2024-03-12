package HW.HW9;

class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    public TreeNode(int root) {
        this.value = root;
        this.left = null;
        this.right = null;
    }

    public int lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return -1;
        
            // if p and q are smaller than current node, explore left subtree
        if (p.value < root.value && q.value < root.value) {
            return lowestCommonAncestor(root.left, p, q);
        } else if (p.value > root.value && q.value > root.value) {
            // if p and q are larger than current node, explore right subtree
            return lowestCommonAncestor(root.right, p, q);
        } else {
            // if nothing is both smaller and greater, its the lca
            return root.value;
        }//if elses
    } //lowest common ancestor
} //treenode

public class Main {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(3);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(1);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(9);

        System.out.println("LCA: " + root.lowestCommonAncestor(root, root.left.left, root.right.left)); // testcase 1 (p:1 q:5, answer: 4)
        System.out.println("LCA: " + root.lowestCommonAncestor(root, root.left, root.left.left)); // testcase 2 (p:3 q:1, answer: 3)
    }
}
