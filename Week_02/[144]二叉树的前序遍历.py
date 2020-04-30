# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []

        def _preorder1(node):
            """
            递归
            :param node:
            :return:
            """
            if not node: return
            self.res.append(node.val)
            _preorder1(node.left)
            _preorder1(node.right)

        def _preorder2(node):
            """
            stack模拟递归
            前序遍历：根左右，先写入根结点的val，再按照左右的顺序遍历到叶子结点
            :param node:
            :return:
            """
            if not node: return []
            stack = [node]
            while stack:
                node = stack.pop()
                if node:
                    self.res.append(node.val)
                    stack.extend([node.right, node.left])

        def _preorder3(node):
            """
            stack模拟的高级版
            :param node:
            :return:
            """
            if not node: return []
            stack = [node]
            while stack:
                node = stack.pop()
                if not node: continue
                if isinstance(node, TreeNode):
                    stack.extend([node.right, node.left, node.val])
                else:
                    self.res.append(node)

        _preorder3(root)
        return self.res
# leetcode submit region end(Prohibit modification and deletion)
