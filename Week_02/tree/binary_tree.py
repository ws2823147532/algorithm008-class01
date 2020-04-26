from queue import Queue

from Week_02.tree.abstract_tree import AbstractTree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS 的复杂度分析
# 时间复杂度：
#   我们每个结点只访问一次，因此时间复杂度为 O(N)，其中 N 是结点的数量。
# 空间复杂度：
#   在最糟糕的情况下，树是完全不平衡的，例如每个结点只剩下左子结点，递归将会被调用 N 次（树的高度），因此保持调用栈的存储将是 O(N)。
#   但在最好的情况下（树是完全平衡的），树的高度将是 O(logN)。因此，在这种情况下的空间复杂度将是 O(logN)。

class BinaryTree(AbstractTree):
    def __init__(self):
        super().__init__()
        self.root = None

    def __str__(self):
        pass

    def root(self):
        return self.root

    def is_empty(self):
        return self.root is not None

    def left_child(self, x):
        pass

    def right_sibling(self, x):
        pass

    def _depth(self, root: TreeNode):
        """
        DFS方式
        :param root:
        :return:
        """
        if not root: return 0
        return max(self._depth(root.left), self._depth(root.right)) + 1

    def _depth1(self, root: TreeNode):
        """
        BFS方式
        按照层次遍历，遍历完一层，深度加1
        :param root:
        :return:
        """
        if not root: return 0
        depth = 1
        queue = Queue()
        queue.put((1, root))
        while not queue.empty():
            depth, node = queue.get()
            if node.left:
                queue.put((depth + 1, node.left))
            if node.right:
                queue.put((depth + 1, node.right))
        return depth

    def depth(self):
        return self._depth1(self.root)

    def traveling(self):
        """
        默认选择 DFS-前序遍历
        :return:
        """
        self.pre_traveling()

    def pre_traveling(self):
        """
        DFS-前序遍历
        :return:
        """
        pass

    def in_order_traveling(self):
        """
        DFS-中序遍历：左-中右
        :return:
        """
        self.res = []

        def _inorder1(node):
            """
            递归的实现方式
            :param node:
            :return:
            """
            if not node: return
            _inorder1(node.left)
            self.res.append(node.val)
            _inorder1(node.right)

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

        _inorder1(self.root)
        return self.res

    def post_order_traveling(self):
        """
        DFS-后序遍历
        :return:
        """
        pass

    def level_traveling(self):
        """
        BFS-层次遍历
        :return:
        """
        pass

    def longest_path(self, x):
        """
        找到
        :param x:
        :return:
        """
        return self._depth1(x) - 1
