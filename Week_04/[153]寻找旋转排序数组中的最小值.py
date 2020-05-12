# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
#  请找出其中最小的元素。
#
#  你可以假设数组中不存在重复元素。
#
#  示例 1:
#
#  输入: [3,4,5,1,2]
# 输出: 1
#
#  示例 2:
#
#  输入: [4,5,6,7,0,1,2]
# 输出: 0
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return None
        tmp = nums[0]
        for num in nums:
            if num < tmp:
                return num
        return tmp

    # 二分法：
    def findMin1(self, nums: List[int]) -> int:
        # 没有旋转的情况
        if nums[0] <= nums[-1]: return nums[0]
        l, r, first = 0, len(nums) - 1, nums[0]

        while l <= r:
            mid = (l + r) >> 1
            # 前面的值大于mid，说明：最小值在mid之前，否则在mid之后
            if first > nums[mid]:
                if nums[mid] < nums[mid - 1]:
                    return nums[mid]
                r = mid - 1
            else:
                if nums[mid] > nums[mid + 1]:
                    return nums[mid + 1]
                l = mid + 1


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().findMin([3, 4, 5, 1, 2])
print(res)
