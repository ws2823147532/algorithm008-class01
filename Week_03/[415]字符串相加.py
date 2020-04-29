# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
#  注意：
#
#
#  num1 和num2 的长度都小于 5100.
#  num1 和num2 都只包含数字 0-9.
#  num1 和num2 都不包含任何前导零。
#  你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
#
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            return self.addStrings(num2, num1)
        l, l1 = len(num1), len(num2)
        jinwei = 0
        res = [str(0)] * (l + 1)
        for i in range(l - 1, -1, -1):
            tmp = num2[i - (l - l1)] if i - (l - l1) >= 0 else 0
            digit = int(num1[i]) + int(tmp) + jinwei
            jinwei = 1 if digit >= 10 else 0
            res[i + 1] = str(digit % 10)
            res[i] = str(jinwei)
        return ''.join(res) if res[0] != '0' else ''.join(res[1:])


# leetcode submit region end(Prohibit modification and deletion)

res = Solution().addStrings('1', '1')
print(res)
