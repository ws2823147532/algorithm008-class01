# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#  注意：给定 n 是一个正整数。
#
#  示例 1：
#
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
#  示例 2：
#
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
# 方法一：递归方式(优化：记忆式递归)
# steps(n) = steps(n-1) + steps(n-2)
# 终止条件：if n=1 return 1
# 方法二、动态规划
class Solution:
    tmp_res = {}

    def climbStairs(self, n: int) -> int:
        if n in self.tmp_res:
            return self.tmp_res[n]
        if n == 1 or n == 0:
            return 1

        self.tmp_res[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.tmp_res[n]


# leetcode submit region end(Prohibit modification and deletion)


res = Solution().climbStairs(6)
print(res)
