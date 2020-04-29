# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例：
#
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)

# 暴力解法：三层循环，时间复杂度太高
# 可以利用排序后的 有序数组的特点加速遍历
# 定义一个移动的指针i，p1和p2分别从i的下一位和最后一位向对方夹逼，直到nums[i]>0 or i=len(nums)-2
#  i p1---------->----<---------p2
# 注意：处理重复的情况，当num[i]连续一样的时候，需要跨越过去，因为后续的结果肯定和第一个nums[i]的结果一样

class Solution:
    def threeSum(self, nums):
        if not nums: return
        i = 0
        res = []
        nums.sort()
        l = len(nums)
        while nums[i] <= 0 and i < l - 2:
            while 0 < i < l - 2 and nums[i] == nums[i - 1]:
                i += 1
            p1, p2 = i + 1, l - 1
            while p1 < p2:
                if nums[i] + nums[p1] + nums[p2] == 0:
                    res.append([nums[i], nums[p1], nums[p2]])
                    p1, p2 = p1 + 1, p2 - 1
                    while p1 < p2 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1
                elif nums[i] + nums[p1] + nums[p2] < 0:
                    p1 += 1
                else:
                    p2 -= 1
            i += 1

        return res

    def threeSum1(self, nums):
        pass


# leetcode submit region end(Prohibit modification and deletion)

res = Solution().threeSum([0, 0, 0, 0])
print(res)
