# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
#  说明：不要使用任何内置的库函数，如 sqrt。
#
#  示例 1：
#
#  输入：16
# 输出：True
#
#  示例 2：
#
#  输入：14
# 输出：False
#
#  Related Topics 数学 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPerfectSquare1(self, num: int) -> bool:
        l, r = 0, num

        while l <= r:
            mid = (l + r) >> 1
            square = mid * mid
            if square <= num:
                l = mid + 1
                if square == num: return True
            else:
                r = mid - 1
        return False

    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().isPerfectSquare(5)
print(res)
