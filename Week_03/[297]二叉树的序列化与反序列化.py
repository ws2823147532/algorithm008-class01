# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
# 式重构得到原数据。
#
#  请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
# 反序列化为原始的树结构。
#
#  示例:
#
#  你可以将以下二叉树：
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# 序列化为 "[1,2,3,null,null,4,5]"
#
#  提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这
# 个问题。
#
#  说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
#  Related Topics 树 设计


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def set_left(self, left):
        self.left = left
        return self

    def set_right(self, right):
        self.right = right
        return self

    def __str__(self):
        return str(self.val)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def func(node):
            if not node:
                res.append('None')
                return
            res.append(str(node.val))
            func(node.left)
            func(node.right)

        func(root)

        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')

        def func():
            if vals:
                if vals[0] == 'None':
                    vals.pop(0)
                    return None
                root = TreeNode(vals[0])
                vals.pop(0)
                root.left = func()
                root.right = func()
                return root

        return func()

    def serialize1(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')

        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize1(self, data):
        """
        相较于第一种方法，这种方法避免了vals.pop(0)的时间复杂度
        :param data:
        :return:
        """

        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node

        vals = iter(data.split())
        return doit()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)

# root = TreeNode(1).set_left(
#     TreeNode(2).set_left(
#         TreeNode(3)
#     ).set_right(
#         TreeNode(4)
#     )
# ).set_right(
#     TreeNode(5)
# )
#
# res = Codec().serialize(root)
# print(res)

res = Codec().deserialize('1,2,3,None,None,4,None,None,5,None,None')
print(res)
