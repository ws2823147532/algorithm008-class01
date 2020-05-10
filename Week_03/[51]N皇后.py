# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
#  上图为 8 皇后问题的一种解法。
#
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#  示例:
#
#  输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#
#
#
#
#  提示：
#
#
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或七步
# ，可进可退。（引用自 百度百科 - 皇后 ）
#
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 每下降一层，查看左上、上、右上三个位置是否有皇后。如果当前层没有可以放置皇后的位置，那么进行回溯
from typing import List


class Solution:
    # 暴力版本
    def solveNQueens1(self, n: int) -> List[List[str]]:
        def cal_forward(forwards, level):
            _forwards = []
            for i in range(level):
                _forwards.extend([(forward[0] + forward[0] * i, forward[1] + forward[1] * i) for forward in forwards])
            return _forwards

        def cal_pos(pos, d):
            return pos[0] + d[0], pos[1] + d[1]

        def is_valid(pos):
            return 0 <= pos[0] < n and 0 <= pos[1] < n

        def ca_put_queen(positions):
            return sum([board[pos[0]][pos[1]] == 'Q' for pos in positions]) == 0

        board = [['.'] * n for i in range(n)]
        res = []
        forwards = [(-1, -1), (-1, 0), (-1, 1)]

        def backtrack(level):
            # 终止条件
            if level == n:
                res.append([''.join(line) for line in board])
                return

            # 处理当前层逻辑
            have_queen = False
            for pos in range(n):
                # 计算当前pos的所有合法的检测位置
                target_pos = [
                    cal_pos((level, pos), forward) for forward in cal_forward(forwards, level)
                    if is_valid(cal_pos((level, pos), forward))
                ]
                # 检测所有合法检测位置是否有queen，都没有，那么把当前pos置为Q，继续到下一层
                if ca_put_queen(target_pos):
                    have_queen = True
                    board[level][pos] = 'Q'

                    # drill down到下一层
                    backtrack(level + 1)
                    # revert state
                    board[level][pos] = '.'
            if not have_queen: return

        backtrack(0)
        return res

    # 剪枝版本
    def solveNQueens2(self, n: int) -> List[List[str]]:

        def is_valid(pos):
            return 0 <= pos[0] < n and 0 <= pos[1] < n

        def cal_pos(pos, d):
            return pos[0] + d[0], pos[1] + d[1]

        def ca_put_queen(pos, forwards, level):
            for i in range(level):
                for forward in forwards:
                    target_pos = cal_pos(pos, (forward[0] + forward[0] * i, forward[1] + forward[1] * i))
                    if is_valid(target_pos) and board[target_pos[0]][target_pos[1]] == 'Q':
                        return False
            return True

        board = [['.'] * n for i in range(n)]
        res = []
        forwards = [(-1, -1), (-1, 0), (-1, 1)]

        def backtrack(level):
            # 终止条件
            if level == n:
                res.append([''.join(line) for line in board])
                return

            # 处理当前层逻辑
            for pos in range(n):
                # 检测所有合法检测位置是否有queen，都没有，那么把当前pos置为Q，继续到下一层
                if ca_put_queen((level, pos), forwards, level):
                    board[level][pos] = 'Q'

                    # drill down到下一层
                    backtrack(level + 1)
                    # revert state
                    board[level][pos] = '.'

        backtrack(0)
        return res

    # 剪枝版本，最后构造结果集
    def solveNQueens(self, n: int) -> List[List[str]]:

        def is_valid(pos):
            return 0 <= pos[0] < n and 0 <= pos[1] < n

        def cal_pos(pos, d):
            return pos[0] + d[0], pos[1] + d[1]

        def ca_put_queen(pos, forwards, level):
            for i in range(level):
                for forward in forwards:
                    target_pos = cal_pos(pos, (forward[0] + forward[0] * i, forward[1] + forward[1] * i))
                    if is_valid(target_pos) and board[target_pos[0]][target_pos[1]] == 'Q':
                        return False
            return True

        board = [['.'] * n for i in range(n)]
        res = []
        forwards = [(-1, -1), (-1, 0), (-1, 1)]

        def backtrack(level, queens):
            # 终止条件
            if level == n:
                res.append(queens)
                return

            # 处理当前层逻辑
            for pos in range(n):
                # 检测所有合法检测位置是否有queen，都没有，那么把当前pos置为Q，继续到下一层
                if ca_put_queen((level, pos), forwards, level):
                    board[level][pos] = 'Q'

                    # drill down到下一层
                    backtrack(level + 1, queens + [pos])
                    # revert state
                    board[level][pos] = '.'

        backtrack(0, [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in r] for r in res]

    def solveNQueens3(self, n: int) -> List[List[str]]:
        result = []

        def DFS(level, pie, na, res):
            if level == n:
                result.append(res)
            for i in range(n):
                if i not in res and level + i not in pie and level - i not in na:
                    DFS(level + 1, pie + [level + i], na + [level - i], res + [i])

        DFS(0, [], [], [])

        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in res] for res in result]


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().solveNQueens(4)
print(res)
