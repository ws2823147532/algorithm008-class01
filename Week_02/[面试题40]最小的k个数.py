# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
#
#
#  示例 1：
#
#  输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#
#
#  示例 2：
#
#  输入：arr = [0,1,2,1], k = 1
# 输出：[0]
#
#
#
#  限制：
#
#
#  0 <= k <= arr.length <= 10000
#  0 <= arr[i] <= 10000
#
#  Related Topics 堆 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class BinaryHeap:
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
        return (i - 1) // 2

    @staticmethod
    def _kth_child(i, k):
        return 2 * i + k

    def _heapify_up(self, i):
        """
        从i开始 自下而上的调整整个堆
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
            i = self._father(i)
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
        :return:
        """
        tmp = self.data[i]

        while self._kth_child(i, 1) < len(self.data):
            child = self._valid_child(i)
            if self.comparator(self.data[child], tmp):
                self.data[i] = self.data[child]
            else:
                break
            i = child

        self.data[i] = tmp


class Solution:

    def getLeastNumbers1(self, arr: List[int], k: int) -> List[int]:
        """
        自定义的binary heap耗时360ma
        :param arr:
        :param k:
        :return:
        """
        if not arr or k <= 0: return []
        max_heap = BinaryHeap(heap_type='max')
        max_heap.from_list(arr[:k])

        for num in arr[k:]:
            max_top = max_heap.peek()
            if num < max_top:
                max_heap.pop()
                max_heap.push(num)

        return max_heap.data

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """
        调用库函数，耗时64ms
        :param arr:
        :param k:
        :return:
        """
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        import heapq
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


# leetcode submit region end(Prohibit modification and deletion)

res = Solution().getLeastNumbers([0, 0, 0, 2, 0, 5], 0)
print(res)
