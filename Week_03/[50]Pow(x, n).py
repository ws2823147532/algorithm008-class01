# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
#  示例 1:
#
#  输入: 2.00000, 10
# 输出: 1024.00000
#
#
#  示例 2:
#
#  输入: 2.10000, 3
# 输出: 9.26100
#
#
#  示例 3:
#
#  输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
#
#  说明:
#
#
#  -100.0 < x < 100.0
#  n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
#
#  Related Topics 数学 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 暴力循环： 超时
    def myPow1(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        if n < 0: n, x = -n, 1 / x

        res = 1.0
        for i in range(n):
            res *= x
        return res

    # 递归分治
    def myPow(self, x: float, n: int) -> float:

        def func(x, n):
            # 终结条件
            if n == 0: return 1.0
            # 当前层
            # 下钻 & merge
            res = func(x, n >> 1)  # func(x, n // 2)
            return (res * res) if n & 1 == 0 else (res * res * x)  # n % 2 == 0
            # revert state

        if n < 0: n, x = -n, 1 / x
        return func(x, n)

    def myPow2(self, x: float, n: int) -> float:
        def subpow(x, n):
            if n == 0: return 1
            if n == 1: return x
            result = subpow(x, n >> 1)
            result *= result
            if n & 1: result *= x
            return result

        if x == 0: return 0
        if n == 0: return 1
        if n > 0: return subpow(x, n)
        n = -n
        return 1 / subpow(x, n)


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().myPow(2.0, 10)
print(res)
