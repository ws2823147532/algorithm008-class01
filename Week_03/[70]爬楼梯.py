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
# 方法一：递归方式(优化：记忆式递归)  就不写了
# steps(n) = steps(n-1) + steps(n-2)
# 终止条件：if n=1 return 1
# 方法二、动态规划  虽然不是很理解，但是写一下吧
# 第一阶  1种方法  走一阶
# 第二阶  2种方法  走一阶或二阶
# 同时我们发现，在第i阶看的话，能达到第i阶只有走一阶或两阶，也就是说到达第阶的方式应该是到达第i-1阶和i-2阶的和
class Solution:

    def climbStairs(self, n: int) -> int:
        res = [1, 2] + [0] * (n - 2)
        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]

        return res[n - 1]


# leetcode submit region end(Prohibit modification and deletion)

res = Solution().climbStairs(3)
print(res)
