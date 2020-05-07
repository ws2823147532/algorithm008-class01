# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
#  示例 1:
#
#  输入: [3,2,3]
# 输出: 3
#
#  示例 2:
#
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#  Related Topics 位运算 数组 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
# 寻找多数元素(并不是准确的众数)的方法
#     计数法：hash表，记录频次
#     排序法：排序取中间的元素
#         一个有序数组的中间位置肯定是  多数元素 [次数大于 ⌊ n/2 ⌋ 的元素]
#     随机法
#         每次可以把不满足条件的元素删除掉，再选，那么 多数元素 被选中的概率就会 越来越大
#     递归分治法  ✅
#         原理：如果将整体分为两部分，那么整体的 众数 一定是这两部分的 众数 之一。
#         选择条件，比较两部分的众数的频次
#     投票法
#         每个候选人给所有候选人投票，当票数为0时，替换候选人。最后剩下的人肯定就是当选者
from typing import List


class Solution:
    @staticmethod
    def _frequency(nums, num):
        return sum(1 for i in nums if i == num)

    # 分治
    def majorityElement1(self, nums: List[int]) -> int:
        def func(l, r):
            # 终结条件
            if l == r: return nums[l]
            # 当前层逻辑
            mid = (l + r) // 2
            # 下钻到一下层  merge
            left = func(l, mid)
            right = func(mid + 1, r)
            if left == right: return left

            left_cnt = self._frequency(nums[l:r + 1], left)
            right_cnt = self._frequency(nums[l:r + 1], right)
            return left if left_cnt > right_cnt else right

        return func(0, len(nums) - 1)

    # 随机法
    def majorityElement2(self, nums: List[int]) -> int:
        l = len(nums) // 2
        import random
        while True:
            candidate = random.choice(nums)
            cnt = self._frequency(nums, candidate)
            if cnt <= l:
                nums.remove(candidate)
            else:
                return candidate

    # 投票法
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        vote = 0
        for num in nums:
            if vote == 0: candidate = num
            if candidate == num:
                vote += 1
            else:
                vote -= 1

        return candidate


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().majorityElement([2, 2, 2, 1, 1, 1, 1, 2, 2])
print(res)
