# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
#  注意:
# 你可以假设树中没有重复的元素。
#
#  例如，给出
#
#  中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  Related Topics 树 深度优先搜索 数组


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 中序遍历：左根右
    # 后序遍历：左右根
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return

        root_val = postorder[-1]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])

        return root
# leetcode submit region end(Prohibit modification and deletion)
