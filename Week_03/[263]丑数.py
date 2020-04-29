# 编写一个程序判断给定的数是否为丑数。
#
#  丑数就是只包含质因数 2, 3, 5 的正整数。
#
#  示例 1:
#
#  输入: 6
# 输出: true
# 解释: 6 = 2 × 3
#
#  示例 2:
#
#  输入: 8
# 输出: true
# 解释: 8 = 2 × 2 × 2
#
#
#  示例 3:
#
#  输入: 14
# 输出: false
# 解释: 14 不是丑数，因为它包含了另外一个质因数 7。
#
#  说明：
#
#
#  1 是丑数。
#  输入不会超过 32 位有符号整数的范围: [−231, 231 − 1]。
#
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
# 满足2a+3b+5c=num格式的数为丑数
class Solution:
    def isUgly(self, num: int) -> bool:

        def search(num):
            # recursion terminator
            if num == 1:
                return True
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
                return False

            # prepare date
            # ...

            # conquer sub-problems
            res_2 = search(num / 2) if num % 2 == 0 else False
            res_3 = search(num / 3) if num % 3 == 0 else False
            res_5 = search(num / 5) if num % 5 == 0 else False

            # process and generate the final result
            return res_2 or res_3 or res_5

        if num < 1: return False
        return search(num)
# leetcode submit region end(Prohibit modification and deletion)
