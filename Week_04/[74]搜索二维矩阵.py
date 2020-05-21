# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#
#  每行中的整数从左到右按升序排列。
#  每行的第一个整数大于前一行的最后一个整数。
#
#
#  示例 1:
#
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#
#
#  示例 2:
#
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False

        def binary_search(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] == target: return True
                if nums[mid] < target: left = mid + 1
                if nums[mid] > target: right = mid - 1
            return False

        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][len(matrix[i]) - 1]:
                return binary_search(matrix[i])

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False

        def binary_search(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] == target: return True
                if nums[mid] < target: left = mid + 1
                if nums[mid] > target: right = mid - 1
            return False

        left, right, step = 0, len(matrix) - 1, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) >> 1
            if matrix[mid][0] <= target <= matrix[mid][step]:
                return binary_search(matrix[mid])
            if matrix[mid][0] > target: right = mid - 1
            if matrix[mid][step] < target: left = mid + 1

        return False

# leetcode submit region end(Prohibit modification and deletion)
