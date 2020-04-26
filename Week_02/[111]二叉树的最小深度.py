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
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        BFS方式
        按照层次遍历，遍历完一层，深度加1
        :param root:
        :return:
        """
        if not root: return 0
        depth = 1
        from queue import Queue
        queue = Queue()
        queue.put((1, root))
        while not queue.empty():
            depth, node = queue.get()
            if node.left:
                queue.put((depth + 1, node.left))
            if node.right:
                queue.put((depth + 1, node.right))
        return depth

    def maxDepth1(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# leetcode submit region end(Prohibit modification and deletion)
