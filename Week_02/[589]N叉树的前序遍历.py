# 给定一个 N 叉树，返回其节点值的前序遍历。
#
#  例如，给定一个 3叉树 :
#
#
#
#
#
#
#
#  返回其前序遍历: [1,3,5,6,2,4]。
#
#
#
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


# 前序遍历：根->children
class Solution:
    def preorder1(self, root: 'Node') -> List[int]:
        res = []

        def func(node):
            if not node: return
            res.append(node.val)

            for _node in node.children:
                func(_node)

        func(root)
        return res

    def preorder2(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []
        q = [root]
        while q:
            curr = q.pop()
            res.append(curr.val)
            if curr:
                q.extend(reversed(curr.children))
                # for i in range(len(curr.children) - 1, -1, -1):
                #     q.append(curr.children[i])
        return res

    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = []
        q = [root]
        while q:
            curr = q.pop()
            if isinstance(curr, Node):
                q.extend(list(reversed(curr.children)) + [curr.val])
            else:
                res.append(curr)

        return res

# leetcode submit region end(Prohibit modification and deletion)
