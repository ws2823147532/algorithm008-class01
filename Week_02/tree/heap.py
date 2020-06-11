class BinaryHeap:
    """
    大顶堆：根节点是最大值,根结点要比所有子树都大
    小顶堆：根节点是最小值,根结点要比左右子树都小
    """

    def __init__(self, heap_type='min'):
        self.data = []

        # min 小顶堆：根结点要比左右子树都小
        # max 大顶堆：根结点要比所有子树都大
        self.heap_type = heap_type
        self.comparator = (lambda x, y: x < y) if heap_type == 'min' else (lambda x, y: x > y)

    def __str__(self):
        return f'{self.heap_type}: {self.data}'

    def from_list(self, vals):
        for val in vals:
            self.push(val)

    def push(self, val):
        """
        向堆中插入一个元素
        将元素追加到最后，然后向上调整
        :param val:
        :return:
        """
        self.data.append(val)
        self._heapify_up(len(self.data) - 1)

    def pop(self):
        """
        删除后并返回堆顶元素
        :return:
        """
        lastelt = self.data.pop()
        if self.data:
            top = self.data[0]
            self.data[0] = lastelt
            self._heapify_down(0)
            return top
        return lastelt

    def peek(self):
        """
        仅返回堆顶元素
        :return:
        """
        if self.data:
            return self.data[0]

    def index_of(self, val):
        """
        返回val的index
        :param val:
        :return:
        """
        if self.data:
            for i in range(len(self.data)):
                if val == self.data[i]:
                    return i
        return -1

    def remove(self, val):
        """
        删除指定的元素
        :param val:
        :return:
        """
        index = self.index_of(val)
        if index == -1: return False
        self._remove_at(index)
        return True

    def _remove_at(self, index):
        """
        移除指定index的元素
        :param index:
        :return:
        """
        moved = self.data.pop()
        self.data[index] = moved
        self._heapify_down(index)
        if self.data[index] == moved:
            self._heapify_up(index)

    @staticmethod
    def _father(i):
        # return (i - 1) // 2
        return (i - 1) >> 1

    @staticmethod
    def _kth_child(i, k):
        """
        获取第i个元素的第k个孩子的索引
        :return:
        """
        return 2 * i + k

    def _heapify_up(self, i):
        """
        从i开始 自下而上的调整整个堆
        记录待调整元素
        待调整元素与父结点比较
            小顶堆：
                如果小于父结点元素，则将父结点向下调整，继续向上
        :return:
        """
        # while True:
        #     # 已经到了根结点了
        #     if i == 0: break
        #     f_i = self._father(i)
        #     if self.comparator(self.data[i], self.data[f_i]):
        #         self.data[i], self.data[f_i] = self.data[f_i], self.data[i]
        #         i = f_i
        #     # 当前元素与其父结点相比，已经不再满足条件
        #     else:
        #         break
        insert_val = self.data[i]
        while i > 0 and self.comparator(insert_val, self.data[self._father(i)]):
            self.data[i] = self.data[self._father(i)]
            i = self._father(i)  # 持续向上调整
        self.data[i] = insert_val

    def _valid_child(self, i):
        """
        返回当前结点两个子结点中满足comparator定义的结点
        :return:
        """
        l_child = self._kth_child(i, 1)
        r_child = self._kth_child(i, 2)
        return l_child \
            if r_child >= len(self.data) or self.comparator(self.data[l_child], self.data[r_child]) \
            else r_child

    def _heapify_down(self, i):
        """
        从i开始 自上而下的调整整个堆
        选择最大(小)的孩子节点进行交换，直到比所有的孩子节点都大(小)
        :return:
        """
        tmp = self.data[i]

        while self._kth_child(i, 1) < len(self.data):
            child = self._valid_child(i)  # 选择最大孩子节点
            if self.comparator(self.data[child], tmp):
                self.data[i] = self.data[child]
            else:
                break
            i = child  # 持续向下调整

        self.data[i] = tmp


min_heap = BinaryHeap(heap_type='max')
min_heap.from_list([3, 2, 1])
print(min_heap)
