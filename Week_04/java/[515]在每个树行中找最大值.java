//您需要在二叉树的每一行中找到最大的值。
//
// 示例：
//
//
//输入:
//
//          1
//         / \
//        3   2
//       / \   \
//      5   3   9
//
//输出: [1, 3, 9]
//
// Related Topics 树 深度优先搜索 广度优先搜索


//leetcode submit region begin(Prohibit modification and deletion)

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public List<Integer> largestValues(TreeNode root) {
        if (root == null) return new ArrayList<Integer>();

        Deque<TreeNode> deque = new ArrayDeque<TreeNode>();
        TreeNode levelFlag = new TreeNode(Integer.MIN_VALUE);
        deque.addLast(levelFlag);
        int level = -1;
        deque.addLast(root);
        List<Integer> ans = new ArrayList<Integer>();
        int levelMax = Integer.MIN_VALUE;

        while (!deque.isEmpty()) {
            TreeNode currNode = deque.pollFirst();
            if (currNode == levelFlag) { // 遍历到了分界点
                if (level >= 0) {
                    ans.add(levelMax);
                }
                levelMax = Integer.MIN_VALUE;
                level += 1;
                if (!deque.isEmpty()) {
                    deque.addLast(levelFlag); // deque不为空，插入分界标记
                }
                currNode = deque.pollFirst(); // 继续取出分界点的下一个节点作为当前接节点
            }
            if (currNode != null && currNode != levelFlag) {
                levelMax = Math.max(levelMax, currNode.val);
                if (currNode.left != null) {
                    deque.addLast(currNode.left);
                }
                if (currNode.right != null) {
                    deque.addLast(currNode.right);
                }
            }
        }
        return ans;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
