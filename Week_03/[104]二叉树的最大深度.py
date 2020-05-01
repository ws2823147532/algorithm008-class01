# 给定一个二叉树，找出其最大深度。
#
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回它的最大深度 3 。
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        stack模拟递归实现，原理：stack是陷入后出，那么可以用stack来模拟树的前中后序遍历，即可得到树的最大深度
        只需要记录当前节点的level，这里使用前序遍历方便些
        :param root:
        :return:
        """
        if not root: return 0
        stack = [(1, root)]
        max_depth = 1
        while stack:
            level, node = stack.pop()
            if node:
                max_depth = level
            stack.extend([(level + 1, root.right), (level + 1, root.left)])

        return max_depth

    def maxDepth1(self, root: TreeNode) -> int:
        """
        递归：树 的最大深度=max(左，右)+1
        :param root:
        :return:
        """
        if not root: return 0
        return max(self.maxDepth1(root.left), self.maxDepth1(root.right)) + 1

# leetcode submit region end(Prohibit modification and deletion)
