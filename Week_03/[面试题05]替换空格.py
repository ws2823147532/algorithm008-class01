# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
#
#
#
#  示例 1：
#
#  输入：s = "We are happy."
# 输出："We%20are%20happy."
#
#
#
#  限制：
#
#  0 <= s 的长度 <= 10000
#


# leetcode submit region begin(Prohibit modification and deletion)
import re


class Solution:
    def replaceSpace1(self, s: str) -> str:
        # return re.sub(' ', '%20', s)
        return s.replace(' ', '%20')

    def replaceSpace2(self, s: str) -> str:
        return ''.join([('%20' if c == ' ' else c) for c in s])

    def replaceSpace(self, s: str) -> str:
        res = ''
        for c in s: res += '%20' if c == ' ' else c
        return res


# leetcode submit region end(Prohibit modification and deletion)

res = Solution().replaceSpace1('We are  happy.')
print(res)
