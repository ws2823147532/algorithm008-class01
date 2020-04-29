# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# 暴力解法：两遍循环
# 排序 之后双指针 夹逼   然而这道题不能 破坏原来的位置
# 使用哈希表记录目标值，加速循环   使用这种方式

class Solution:
    def twoSum(self, nums, target):
        if not nums: return

        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return [map[nums[i]], i]


# leetcode submit region end(Prohibit modification and deletion)


res = Solution().twoSum([2, 7, 11, 15], 9)
print(res)
