# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。
#
#  一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列
# ，而 "AEC" 不是）
#
#  题目数据保证答案符合 32 位带符号整数范围。
#
#
#
#  示例 1：
#
#  输入：S = "rabbbit", T = "rabbit"
# 输出：3
# 解释：
#
# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#
#
#  示例 2：
#
#  输入：S = "babgbag", T = "bag"
# 输出：5
# 解释：
#
# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
# (上箭头符号 ^ 表示选取的字母)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] 表示t的前i个字符可以通过s的前j个字符构成的个数，dp[0][...]=1
        dp = [[1 if j == 0 else 0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]

        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[len(t)][len(s)]


# leetcode submit region end(Prohibit modification and deletion)

res = Solution().numDistinct('babgbag', 'bag')
print(res)
