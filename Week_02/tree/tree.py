class Tree:
    """
    定义Tree的模板方法
    """

    def create_tree(self, nodes):
        """
        创建一棵树
        :return:
        """
        pass

    def root(self):
        """
        求树的根节点
        :return:
        """
        pass

    def is_empty(self):
        """
        树是否为空树
        :return:
        """
        pass

    def parent(self, x):
        """
        求指定节点的双亲节点
        :param x:
        :return:
        """
        pass

    def left_child(self, x):
        """
        求某节点的最左子节点
        :param x:
        :return:
        """
        pass

    def right_sibling(self, x):
        """
        求某节点的右兄弟节点
        :param x:
        :return:
        """
        pass

    def traveling(self):
        """
        遍历树
        :return:
        """
        pass

    def depth(self):
        """
        求树的深度
        :return:
        """
        pass

    def insert(self, x):
        """
        插入一个节点
        :param x:
        :return:
        """
        pass

    def delete(self, x):
        """
        删除某个节点
        :param x:
        :return:
        """
        pass
