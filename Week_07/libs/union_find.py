class UnionFind:
    """
    并查集
    """

    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.count = n

    def union(self, i, j):
        """
        把j当做i的parent
        """
        p1 = self.parent(i)
        p2 = self.parent(j)
        if p1 != p2:
            self.p[p1] = p2
            self.count -= 1

    def parent(self, i):
        root = i
        while self.p[root] != root:
            root = self.p[root]

        # while self.p[i] != i:
        #     x, i, self.p[x] = i, self.p[i], root
        while self.p[i] != i:
            # i, self.p[i] = self.p[i], root  # 注意：这里不能用这种写法，因为修改了i的值之后，self.p[i]就会立刻指向修改后的i的位置。这里和普通的a b交换有区别
            self.p[i], i = root, self.p[i]  # 可以
            # x = i
            # i = self.p[i]
            # self.p[x] = root

        return root


uf = UnionFind(6)
uf.union(1, 0)
uf.union(3, 2)
uf.union(4, 0)
uf.union(4, 2)
uf.union(4, 1)

print(uf)
