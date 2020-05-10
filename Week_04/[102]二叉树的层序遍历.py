# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
#  示例：
# 二叉树：[3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其层次遍历结果：
#
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
#  Related Topics 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        import collections
        q = collections.deque()
        q.append(root)
        res = []
        _res = []
        _q = collections.deque()
        while q:
            curr = q.popleft()
            if curr:
                _res.append(curr.val)
                _q.extend([curr.left, curr.right])
            if not q:
                q, _q = _q, q
                if _res:
                    res.append(_res[:])
                _res.clear()
                _q.clear()

        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = [root]
        res = []
        while q:
            _q = []
            _res = []
            for node in q:
                if node:
                    _res.append(node.val)
                    if node.left: _q.append(node.left)
                    if node.right: _q.append(node.right)
            res.append(_res[:])
            q = _q[:]
        return res

    def levelOrder(self, root):
        nodes = [(root,)]
        values = []
        while nodes:
            values.append([r.val for n in nodes for r in n if r])
            nodes = [(r.left, r.right) for n in nodes for r in n if r]
        return values[:-1]

# leetcode submit region end(Prohibit modification and deletion)
