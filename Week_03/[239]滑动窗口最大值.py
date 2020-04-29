# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
#
#  返回滑动窗口中的最大值。
#
#
#
#  进阶：
#
#  你能在线性时间复杂度内解决此题吗？
#
#
#
#  示例:
#
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^5
#  -10^4 <= nums[i] <= 10^4
#  1 <= k <= nums.length
#
#  Related Topics 堆 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
# 思路： 写入窗口的k个数字
# 使用双端队列，维护一个k个元素的窗口，队首是最大值，队尾是较小的值
# 当有一个新的元素进来的时候，检查当前的索引是否是队首的索引+k，是的话，则将队首元素pop
# 当新加进来一个元素，从队尾开始比较，把小于当前元素的索引pop，直到遇到一个比当前元素大的索引
from collections import deque
from typing import List


class Solution:
    # 双端队列：O(N)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k: return []
        if k == 1: return nums
        dq = deque(maxlen=k)
        res = []

        # 处理第一个k元素窗口
        for i in range(k):
            # 循环遍历，从队尾开始排除比当前元素小的元素
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)

        res.append(nums[dq[0]])

        # 后续每移动一个位置，即是将窗口往后移动一次
        for i in range(k, len(nums)):
            # 队首已经不属于窗口，需要删除队首元素
            if dq and i == dq[0] + k: dq.popleft()
            # 循环遍历，从队尾开始排除比当前元素小的元素
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            res.append(nums[dq[0]])

        return res

    # 动态规划
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pass


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3)

print(res)
