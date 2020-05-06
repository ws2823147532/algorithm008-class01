# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
#  说明：解集不能包含重复的子集。
#
#  示例:
#
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#  Related Topics 位运算 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
# 思路：在题设的情况下，不需要考虑重复元素的问题  每个元素选或不选
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res = []

        def func(level, selected):
            # 终结条件
            if level == length:
                res.append(selected[:])
                return

            # 不选择当前元素
            func(level + 1, selected)
            # 选择当前元素
            selected.append(nums[level])
            func(level + 1, selected)

            # revert state
            selected.pop()

        func(0, [])
        return res


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().subsets([1, 2, 3])
print(res)
