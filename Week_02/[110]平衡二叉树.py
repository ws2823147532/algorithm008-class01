# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
#  本题中，一棵高度平衡二叉树定义为：
#
#
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
#
#  示例 1:
#
#  给定二叉树 [3,9,20,null,null,15,7]
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回 true 。
#
# 示例 2:
#
#  给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#         1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#
#
#  返回 false 。
#
#
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced1(self, root: TreeNode) -> bool:
        if not root: return True

        def dfs(node):
            if not node: return -1
            return 1 + max(dfs(node.left), dfs(node.right))

        return abs(dfs(root.left) - dfs(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced(self, root: TreeNode) -> bool:

        def recur(node):
            if not node: return 0
            left = recur(node.left)
            if left == -1: return -1
            right = recur(node.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) < 2 else -1

        return recur(root) != -1
# leetcode submit region end(Prohibit modification and deletion)
