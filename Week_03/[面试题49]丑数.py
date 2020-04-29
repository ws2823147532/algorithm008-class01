# 我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
#
#
#
#  示例:
#
#  输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
#  说明:
#
#
#  1 是丑数。
#  n 不超过1690。
#
#
#  注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
# 满足 2a+3b+5c的数 称为丑数，保证求出丑数的序列，那么每次求的时候应该取最小的丑数，这就要用到最小堆来辅助(可以直接用python的heapq)
#     每次从堆中获取最小值，求其丑数，然后再放回堆中，直到找到第n个

# 思路二：动态规划，后续再说吧
from heapq import heappop, heappush


class Solution:
    def __init__(self):
        self.choushu = []
        self.seen = set()
        self.heap = [1]

    def nthUglyNumber(self, n: int) -> int:
        if len(self.choushu) >= n: return self.choushu[n - 1]
        i = len(self.choushu)
        while True:
            top_min = heappop(self.heap)
            self.choushu.append(top_min)
            i += 1
            _choushu = [top_min * c for c in [2, 3, 5]]
            for num in _choushu:
                if num not in self.seen:
                    heappush(self.heap, num)
                    self.seen.add(num)
            if i >= n:
                return self.choushu[n - 1]


# leetcode submit region end(Prohibit modification and deletion)
s = Solution()

print(s.nthUglyNumber(1400))

print(s.nthUglyNumber(10))
