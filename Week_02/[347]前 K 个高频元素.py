# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
#
#
#  示例 1:
#
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
#  示例 2:
#
#  输入: nums = [1], k = 1
# 输出: [1]
#
#
#
#  提示：
#
#
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
#  你可以按任意顺序返回答案。
#
#  Related Topics 堆 哈希表 分桶


import collections
# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from functools import total_ordering
from typing import List


@total_ordering
class Pair:
    def __init__(self, num, freq):
        self.num = num
        self.freq = freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq


class Solution:
    # 思路：先计数，在排序，在python中一句就能搞定
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        return [pair[0] for pair in collections.Counter(nums).most_common(k)]

    # 将上述的过程拆解开来
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        # 计数
        counter = collections.defaultdict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        h = []
        # 维护k个元素的最小堆，新元素比堆顶元素大，那么
        for num, freq in counter.items():
            if len(h) < k:
                heapq.heappush(h, Pair(num, freq))
            else:
                if h[0] < Pair(num, freq):
                    heapq.heappushpop(h, Pair(num, freq))

        # 从最小堆中取出元素
        res = [0] * k
        for i in range(k):
            res[k - i - 1] = heapq.heappop(h).num

        return res

    # 使用桶排序
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        # 计数
        counter = collections.defaultdict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        bucket = [[] for i in range(len(nums))]
        # 桶排序思想
        for num, freq in counter.items():
            bucket[freq - 1].append(num)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
        return res[:k]


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().topKFrequent([3, 0, 1, 0], 1)
print(res)
