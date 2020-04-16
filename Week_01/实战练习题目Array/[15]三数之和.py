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
# a+b+c=0 似乎长得很像a+b=-c，能不能把这个问题转化成两数之和呢？
# 答案是可以的，但是时间复杂度可能会比较高：两数之和的时间复杂度是O(n)，这里应该要把所有的元素都当做c来处理一遍，
# 可想而知，复杂度会变成O(n^2)

class Solution:
    def threeSum(self, nums):
        # 排除特殊情况
        n = len(nums)
        if not nums or n < 3:
            return []
        # 将数据从小到大排序，利用有序数组的特性
        nums.sort()
        res = []

        # O(n)
        for i in range(n):
            # 如果当前元素大于0，由于是已经排好序的数组，那么后面就不会有满足条件的元素组合了
            if nums[i] > 0:
                break

            # 如果当前元素和上一个元素相等，则不用再看，因为结果和上一个元素是一样的
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1  # 左边界
            right = n - 1  # 有边界

            # 循环条件：左边界小于右边界
            # O(n)
            while left < right:
                # 如果满足条件，则保存结果，并且左右边界分别往里移动
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 由于已经是有序的数组，当前满足条件的元素，如果与下一个元素相等，那么就会出现重复的解
                    # 所以这里直接略过
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 由于已经是有序的数组，当前满足条件的元素，如果与下一个元素相等，那么就会出现重复的解
                    # 所以这里直接略过
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

                # 如果元素组合小于0，则向右移动左边界
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1

                # 如果元素组合大于0，则向左移动右边界
                else:
                    right -= 1

        return res


# leetcode submit region end(Prohibit modification and deletion)

res = Solution().threeSum([0, 0, 0])
print(res)
