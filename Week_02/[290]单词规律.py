# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。 
# 
#  这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。 
# 
#  示例1: 
# 
#  输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true 
# 
#  示例 2: 
# 
#  输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false 
# 
#  示例 3: 
# 
#  输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false 
# 
#  示例 4: 
# 
#  输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false 
# 
#  说明: 
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。 
#  Related Topics 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def workPattern(self, pattern, str):
        dict()
        res = str.split()
        return list(map(pattern.index, pattern)) == list(map(res.index, res))

    def wordPattern(self, pattern: str, str: str) -> bool:
        # python3之后的dict是有序的
        str = str.split()
        if len(pattern) != len(str): return False
        p_cnt = {}
        s_cnt = {}
        i = 0
        for p, s in zip(pattern, str):
            if p not in p_cnt: p_cnt[p] = i
            if s not in s_cnt: s_cnt[s] = i
            i += 1
            try:
                if p_cnt[p] != s_cnt[s]: return False
            except KeyError:
                if p in p_cnt or s in s_cnt: return False
        return True

    def wordPattern(self, pattern: str, str: str) -> bool:
        # python3之后的dict是有序的
        str = str.split()
        if len(pattern) != len(str): return False
        p_cnt = {}
        s_cnt = {}
        i = 0
        for p, s in zip(pattern, str):
            p_cnt[p] = [i] if p not in p_cnt else p_cnt[p] + [i]
            s_cnt[s] = [i] if s not in s_cnt else s_cnt[s] + [i]
            i += 1
        for p, s in zip(p_cnt, s_cnt):
            if p_cnt[p] != s_cnt[s]:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)

res = Solution().wordPattern('abbaa', 'dog cat cat dog cat')
print(res)
