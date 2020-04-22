# 有效括号字符串为空 ("")、"(" + A + ")" 或 A + B，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"
# ，"(())()" 和 "(()(()))" 都是有效的括号字符串。 
# 
#  如果有效字符串 S 非空，且不存在将其拆分为 S = A+B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。 
# 
#  给出一个非空有效字符串 S，考虑将其进行原语化分解，使得：S = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。 
# 
#  对 S 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 S 。 
# 
#  
# 
#  示例 1： 
# 
#  输入："(()())(())"
# 输出："()()()"
# 解释：
# 输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
# 删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。 
# 
#  示例 2： 
# 
#  输入："(()())(())(()(()))"
# 输出："()()()()(())"
# 解释：
# 输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
# 删除每个部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。
#  
# 
#  示例 3： 
# 
#  输入："()()"
# 输出：""
# 解释：
# 输入字符串为 "()()"，原语化分解得到 "()" + "()"，
# 删除每个部分中的最外层括号后得到 "" + "" = ""。
#  
# 
#  
# 
#  提示： 
# 
#  
#  S.length <= 10000 
#  S[i] 为 "(" 或 ")" 
#  S 是一个有效括号字符串 
#  
#  Related Topics 栈


# leetcode submit region begin(Prohibit modification and deletion)
# 先用stack找到原语的分解式，每次stack变空，则说明找到一个primitive
# 然后对每个分解式对比首尾是否配对且从左往右遍历的第二个字符是否也配对
class Solution:
    def removeOuterParentheses1(self, S: str) -> str:
        stack = []
        primitives = {}
        i = 0
        # 找到primitives
        for c in S:
            tmp = primitives.get(i, [])
            tmp.append(c)
            primitives[i] = tmp
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
            # 如果当前stack空了，那么说明找到了一个primitive
            # 如果字符串还没有遍历完，那么就继续找下一个primitive
            if len(stack) == 0:
                i += 1

        res = []
        # 对每个primitive进行剥皮
        for k, primitive in primitives.items():
            len_2 = len(primitive) // 2
            if len_2 == 1:
                res.append('')
                continue
            i = 0
            while primitive[i + 1] != ')':
                if primitive[i] == '(' and primitive[2 * len_2 - i - 1] == ')':
                    i += 1
                else:
                    break
            res.extend(primitive[i:2 * len_2 - i])
        return ''.join(res)

    def removeOuterParentheses2(self, S: str) -> str:
        stack = []
        primitives = {}
        i = 0
        # 找到primitives
        for c in S:
            tmp = primitives.get(i, [])
            tmp.append(c)
            primitives[i] = tmp
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
            # 如果当前stack空了，那么说明找到了一个primitive
            # 如果字符串还没有遍历完，那么就继续找下一个primitive
            if len(stack) == 0:
                i += 1

        res = []
        # 对每个primitive进行剥皮：只剥一层
        for k, primitive in primitives.items():
            if primitive[0] == '(' and primitive[-1] == ')':
                res.extend(primitive[1:len(primitive) - 1])
        return ''.join(res)

    def removeOuterParentheses3(self, S: str) -> str:
        stack = []
        primitives = {}
        i = 0
        res = []
        # 找到primitives
        for c in S:
            tmp = primitives.get(i, [])
            tmp.append(c)
            primitives[i] = tmp
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
            # 如果当前stack空了，那么说明找到了一个primitive
            # 如果字符串还没有遍历完，那么就继续找下一个primitive
            if len(stack) == 0:
                # 对每个primitive进行剥皮：只剥一层
                if primitives[i][0] == '(' and primitives[i][-1] == ')':
                    res.extend(primitives[i][1:len(primitives[i]) - 1])
                i += 1

        return ''.join(res)

    def removeOuterParentheses(self, S: str) -> str:
        stack, res, tmp = [], '', ''
        # 找到primitives
        for c in S:
            tmp += c
            if c == '(':
                stack.append(c)
            else:
                stack.pop()
            # 如果当前stack空了，那么说明找到了一个primitive
            # 如果字符串还没有遍历完，那么就继续找下一个primitive
            if len(stack) == 0:
                # 对每个primitive进行剥皮：只剥一层
                res += tmp[1:-1]
                tmp = ''

        return res


# leetcode submit region end(Prohibit modification and deletion)

res = Solution().removeOuterParentheses('()()')
print(res)
