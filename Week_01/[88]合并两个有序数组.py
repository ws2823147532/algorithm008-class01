# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。 
# 
#  
# 
#  说明: 
# 
#  
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。 
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。 
#  
# 
#  
# 
#  示例: 
# 
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6] 
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# 方法一、先合并再排序，没有利用数组已经有序这一特点
# 方法二、双指针：从前往后
# 方法三、双指针：从后往前
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 方式一：数组赋值方法，不加[:]表示赋给了一个新的变量，不是原地操作
        # nums1[:] = sorted(nums1[:m] + nums2[:n])
        # 方式二：
        # i, j = 0, 0
        # nums1_copy = nums1[:m]
        # while i < m and j < n:
        #     if nums1_copy[i] <= nums2[j]:
        #         nums1[i + j] = nums1_copy[i]
        #         i += 1
        #     else:
        #         nums1[i + j] = nums2[j]
        #         j += 1
        # if i >= m:
        #     nums1[i + j:m + n] = nums2[j:]
        # if j >= n:
        #     nums1[i + j:m + n] = nums1_copy[i:]

        # 方法三：
        i, j, p = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        if i < 0:
            nums1[:p + 1] = nums2[:j + 1]
        if j < 0:
            nums1[:p + 1] = nums1[:i + 1]


# leetcode submit region end(Prohibit modification and deletion)

Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
