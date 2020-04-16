# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
#  说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
#
#
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
#  示例：
#
#  输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# 思路：两个指针分别指向数组两端，计算面积；
# 纵坐标小的那一列向纵坐标高的那一列前进，目的：横坐标一直在减少，只有纵坐标增大，才有可能使得面积变大
class Solution:
    def maxArea(self, height) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i <= j:
            if height[i] < height[j]:
                max_area = max(max_area, height[i] * (j - i))
                i += 1
            else:
                max_area = max(max_area, height[j] * (j - i))
                j -= 1

        return max_area


# leetcode submit region end(Prohibit modification and deletion)

res = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print((res))
