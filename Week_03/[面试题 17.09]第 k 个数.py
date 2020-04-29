# 有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，
# 5，7，9，15，21。
#
#  示例 1:
#
#  输入: k = 5
#
# 输出: 9
#
#  Related Topics 堆 队列 数学


# leetcode submit region begin(Prohibit modification and deletion)
from heapq import heappush, heappop


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        seen = set()
        nums = []
        heap = [1]
        i = 0
        while True:
            top_min = heappop(heap)
            nums.append(top_min)
            i += 1
            _nums = [top_min * n for n in [3, 5, 7]]
            for n in _nums:
                if n not in seen:
                    heappush(heap, n)
                    seen.add(n)

            if i >= k:
                return nums[k - 1]


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().getKthMagicNumber(5)
print(res)
