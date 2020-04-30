# 给定一个二叉树，返回它的中序 遍历。
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
# 输出: [1,3,2]
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []

        def _inorder(node):
            """
            使用递归的方式
            :param node:
            :return:
            """
            if not node: return

            _inorder(node.left)
            self.res.append(node.val)
            _inorder(node.right)

        def _inorder2(node):
            """
            遍历的实现方式-stack
            使用stack模拟递归调用的过程
            :param node:
            :return:
            """
            stack = []
            while node or stack:
                # 一直往左子树走，直到左子树为空
                while node:
                    stack.append(node)
                    node = node.left
                # 左子树走到尽头，则从栈顶取出，然后转换成右子树，继续遍历
                node = stack.pop()
                self.res.append(node.val)
                node = node.right

        def _inorder3(node):
            """
            根据leetcode的题解整理出来
            https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
            使用stack的另一种实现方式，简单统一
            首先初始化栈，将根节点加入栈
            依次出栈得到node，直到stack变成空的
            遇到结点类型，那么继续压入 node.right node.val node.left
                ---- 注意这里就是精髓了：首先中序遍历是左中右，stack是后入先出，所以顺序要反过来。
                    如果要是想变成前序遍历(中左右)，那么压入栈的顺序就是 node.right node.left node.val
                    如果要是想变成后序遍历(左右中)，那么压入栈的顺序就是 node.val node.right node.left
                    遍历的三种方式中，左右的相对顺序是不会变的，变的是中结点的次序
            遇到非节点类型，则加入res
            :param node:
            :return:
            """
            stack = [node]
            while stack:
                node = stack.pop()
                if not node: continue
                if isinstance(node, TreeNode):
                    stack.extend([node.right, node.val, node.left])
                else:
                    self.res.append(node)

        _inorder3(root)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
