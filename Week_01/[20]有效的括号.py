# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
#  有效字符串需满足：
#
#
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#
#
#  注意空字符串可被认为是有效字符串。
#
#  示例 1:
#
#  输入: "()"
# 输出: true
#
#
#  示例 2:
#
#  输入: "()[]{}"
# 输出: true
#
#
#  示例 3:
#
#  输入: "(]"
# 输出: false
#
#
#  示例 4:
#
#  输入: "([)]"
# 输出: false
#
#
#  示例 5:
#
#  输入: "{[]}"
# 输出: true
#  Related Topics 栈 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    braces = {'(': ')', '[': ']', '{': '}'}

    # 利用栈的LIFO的特性来操作，左括号的入栈，遇到右括号，则取出栈顶元素与当前元素进行匹配
    # 匹配成功，则继续，否则return False
    def isValid(self, s: str) -> bool:
        if not s: return True
        if len(s) % 2 != 0: return False
        if s[0] not in self.braces: return False
        stack = []
        for c in s:
            if c in self.braces:
                stack.append(c)
            else:
                pop = stack.pop()
                if self.braces[pop] != c:
                    return False
        return len(stack) == 0


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().isValid('){')
print(res)
