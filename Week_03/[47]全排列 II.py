# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
#  示例:
#
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#  Related Topics 回溯算法
# 思考一下，为什么造成了重复，如何在搜索之前就判断这一支会产生重复，从而“剪枝”。<br />

# 利用有序数组的特性(就和之前做15. 三数之和那样)：连续两个一样的值那么他后续的排列肯定是和前一个值的排列是一样的<br /><br />

# 但是这道题，需要我们慎重使用这个特性，因为还需要满足一个条件：判重的同时，还要保证当前所处的level，即前后两个值level相同的情况才可以使用这个特性<br /><br />

# 那么怎么保证前后两个值level相同呢？可以维护一个全局的状态数组，初始都是0(表示不处于任何level)，和数组长度一样，记录每一个值的level，
# 在dfs的时候，动态改变这个状态数组，当前值参与排列的时候，把对应位置的level设置为当前的level，把当前的值和前一个值进行对比，
# 同时当前的level和前一个值的level进行对比，都一样的话，表明是同一个值在当前level被排列了两次，那么在此处剪枝，否则继续<br /><br />
#
# 同时，我们会发现，只要我们知道了前一个相同的值是否还在参与排列，就足够了：同level的值参与排列的时候会自动被revert state(回溯，即状态重置)，
# 只要前一个相同值没有在参与排列，那么说明此时此刻当前值和前一个值实际上就是处于同一个level，否则的话，说明此时此刻当前值和前一个值实际上就是不处于同一个level。
# 那么也就是说我们可以维护一个0 1的状态数组，保证某元素当前有没有被使用就可以了

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        used = [0] * len(nums)
        res = []
        size = len(nums)
        nums.sort()

        def dfs(level: int, selected: list):
            if level == size:
                res.append(selected[:])
                return
            for i in range(size):
                # 判断当前元素在是否已经处于排列中，如果已经处于排列中，那么不应该再次使用
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    selected.append(nums[i])
                    used[i] = 1
                    dfs(level + 1, selected)
                    used[i] = 0
                    selected.pop()

        dfs(0, [])
        return res


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().permuteUnique([1, 1, 2])
print(res)
