//给定一个二叉树，判断其是否是一个有效的二叉搜索树。
//
// 假设一个二叉搜索树具有如下特征：
//
//
// 节点的左子树只包含小于当前节点的数。
// 节点的右子树只包含大于当前节点的数。
// 所有左子树和右子树自身必须也是二叉搜索树。
//
//
// 示例 1:
//
// 输入:
//    2
//   / \
//  1   3
//输出: true
//
//
// 示例 2:
//
// 输入:
//    5
//   / \
//  1   4
//     / \
//    3   6
//输出: false
//解释: 输入为: [5,1,4,null,null,3,6]。
//     根节点的值为 5 ，但是其右子节点值为 4 。
//
// Related Topics 树 深度优先搜索


//leetcode submit region begin(Prohibit modification and deletion)

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    /**
     * 递归
     * @param root
     * @return
     */
    public boolean isValidBST(TreeNode root) {
        return func(root, - Double.MAX_VALUE, Double.MAX_VALUE);
    }

    private boolean func(TreeNode node, double lower, double upper) {
        if (node == null) return true; // 空节点则返回true

        if (node.val >= upper) return false; // 当前节点大于上界
        if (node.val <= lower) return false; // 当前结点小于下界

        boolean left = func(node.left, lower, node.val);// 当前节点是其左子树的上界

        boolean right = func(node.right, node.val, upper);// 当前节点是其右子树的下界

        return left && right;
    }

    /**
     * 中序遍历：是升序的
     *
     * @param root
     * @return
     */
    public boolean isValidBST1(TreeNode root) {
        if (root == null) return true;

        Deque<Object> stack = new ArrayDeque<>();
        stack.offerLast(root);
        double lastVal = - Double.MAX_VALUE;
        while (!stack.isEmpty()) {
            Object curr = stack.pollLast();
            if (curr instanceof String) continue;
            if (curr instanceof TreeNode)
                stack.addAll(Arrays.asList(((TreeNode) curr).right == null ? "null" : ((TreeNode) curr).right, ((TreeNode) curr).val, ((TreeNode) curr).left == null ? "null" : ((TreeNode) curr).left));
            if (!(curr instanceof TreeNode))
                if ((int) curr <= lastVal)
                    return false;
                else lastVal = (int) curr;
        }
        return true;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
