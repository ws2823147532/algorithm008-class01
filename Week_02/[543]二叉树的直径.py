# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
#
#
#  示例 :
# 给定二叉树
#
#            1
#          / \
#         2   3
#        / \
#       4   5
#
#
#  返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
#
#
#  注意：两结点之间的路径长度是以它们之间边的数目表示。
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

# 二叉树的直径定义：任意两个结点路径长度中的最大值
# 路径长度：路径上的结点数-1
# 最长路径：一定是两个叶子结点之间的路径
# 那么 直径问题可以转化成求某个结点的左右子树的深度
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def _depth(node):
            if not node: return 0
            L = _depth(node.left)
            R = _depth(node.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1

        _depth(root)
        return self.ans - 1
# leetcode submit region end(Prohibit modification and deletion)
