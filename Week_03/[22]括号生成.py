# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例：
#
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 往2n个独立的格子里放括号 每个格子都有两种可能，2^2n
# 使用递归的方式
#   关键在于如何判断括号的有效性，合理的做到剪枝操作
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        size = 2 * n

        def dfs(level: int, left, right, selected: str):
            if level == size:
                res.append(selected)
                return
            # if left > right: return
            if left > 0:
                dfs(level + 1, left - 1, right, selected + '(')
            if right > left:
                dfs(level + 1, left, right - 1, selected + ')')

        dfs(0, n, n, '')
        return res


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().generateParenthesis(3)
print(res)
