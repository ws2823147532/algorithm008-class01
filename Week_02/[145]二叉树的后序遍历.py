# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        后序遍历：左右根
        :param root:
        :return:
        """
        self.res = []

        def _post(node):
            """
            递归
            :param node:
            :return:
            """
            if not node: return
            _post(node.left)
            _post(node.right)
            self.res.append(node.val)

        def _post1(node):
            """
            stack模拟
            :param node:
            :return:
            """
            if not node: return
            stack = [(1, node), (0, node.right), (0, node.left)]
            while stack:
                flag, node = stack.pop()
                if not node: continue
                if flag or (not node.left and not node.right):
                    self.res.append(node.val)
                else:
                    stack.extend([(1, node), (0, node.right), (0, node.left)])

        def _post2(node):
            """
            stack模拟高级版
            :param node:
            :return:
            """
            if not node: return
            stack = [node]
            while stack:
                node = stack.pop()
                if not node: continue
                if isinstance(node, TreeNode):
                    stack.extend([node.val, node.right, node.left])
                else:
                    self.res.append(node)

        _post1(root)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
