# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1:
#
#  输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
#
#
#  示例 2:
#
#  输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        """
        DFS:启动DFS的次数即为岛屿的数量
        每次DFS，扫描过的方块设置为0(避免重复扫描)
        :param grid:
        :return:
        """
        if not grid or not grid[0]: return 0
        height = len(grid)
        length = len(grid[0])

        def dfs(i, j):
            # process termitor
            if grid[i][j] == '0': return
            # curr level
            grid[i][j] = '0'
            # drill down
            for _i, _j in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= _i < height and 0 <= _j < length:
                    dfs(_i, _j)

        island = 0
        for i in range(height):
            for j in range(length):
                if grid[i][j] == '1':
                    island += 1
                    dfs(i, j)
        return island

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        stack-模拟DFS
        :param grid:
        :return:
        """
        if not grid or not grid[0]: return 0
        height, length = len(grid), len(grid[0])
        stack = []
        island = 0
        for i in range(height):
            for j in range(length):
                if grid[i][j] == '1':
                    island += 1
                    stack.append((i, j))
                    while stack:
                        _i, _j = stack.pop()
                        for __i, __j in [(_i + 1, _j), (_i - 1, _j), (_i, _j - 1), (_i, _j + 1)]:
                            if 0 <= __i < height and 0 <= __j < length and grid[__i][__j] == '1':
                                stack.append((__i, __j))
                                grid[__i][__j] = '0'
        return island

    def numIslands11(self, grid: List[List[str]]) -> int:
        """
        BFS

        queue.Queue() 一个同步的队列类，内部会涉及加锁解锁的操作，故会有较大的时间花销。
            其内部就是用的collections.deque实现的，故这里最好不要用queue.Queue()，而是直接用collections.deque
        :param grid:
        :return:
        """
        if not grid or not grid[0]: return 0
        height, length = len(grid), len(grid[0])
        import queue
        q = queue.Queue()
        island = 0

        for i in range(height):
            for j in range(length):
                if grid[i][j] == '1':
                    island += 1
                    q.put((i, j), block=False, timeout=0)
                    while not q.empty():
                        _i, _j = q.get(block=False, timeout=0)
                        for __i, __j in [(_i + 1, _j), (_i - 1, _j), (_i, _j - 1), (_i, _j + 1)]:
                            if 0 <= __i < height and 0 <= __j < length and grid[__i][__j] == '1':
                                q.put((__i, __j), block=False, timeout=0)
                                grid[__i][__j] = '0'
        return island

    def numIslands12(self, grid: List[List[str]]) -> int:
        """
        BFS
        :param grid:
        :return:
        """
        if not grid or not grid[0]: return 0
        height, length = len(grid), len(grid[0])
        import collections
        q = collections.deque()
        island = 0

        for i in range(height):
            for j in range(length):
                if grid[i][j] == '1':
                    island += 1
                    q.append((i, j))
                    while q:
                        _i, _j = q.popleft()
                        for __i, __j in [(_i + 1, _j), (_i - 1, _j), (_i, _j - 1), (_i, _j + 1)]:
                            if 0 <= __i < height and 0 <= __j < length and grid[__i][__j] == '1':
                                q.append((__i, __j))
                                grid[__i][__j] = '0'
        return island

# leetcode submit region end(Prohibit modification and deletion)
