# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
#  注意:
# 你可以假设树中没有重复的元素。
#
#  例如，给出
#
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
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

    # 先序遍历：根左右
    # 中序遍历：左根右
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None

        root_val = preorder[0]  # 先序遍历的第一个元素就是当前(子)树的根节点
        root = TreeNode(root_val)

        mid = inorder.index(root_val)  # 从中序遍历中找到根节点序号

        # 构建左子树
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        # 返回根节点
        return root


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(res)
