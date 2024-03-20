import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int root;
    TreeNode left;
    TreeNode right;

    TreeNode(int root) {
        this.root = root;
        left = right = null;
    } //node
}//Node

public class BinaryTree {

    boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        ArrayList<Integer> list = new ArrayList<>();
        readTree(root, list);
        return isInOrder(list);
    }//isvalidbst

    void readTree(TreeNode node, ArrayList<Integer> list) {
        if (node.left != null) readTree(node.left, list);
        list.add(node.root);
        if (node.right != null) readTree(node.right, list);
    }//readtree

    boolean isInOrder(List<Integer> list) {
        for (int i = 1; i < list.size(); i++) {
            if (list.get(i - 1) >= list.get(i)) return false;
        }//for
        return true;
    }//isinorder
}//binary tree