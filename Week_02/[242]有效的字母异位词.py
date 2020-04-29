# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
#  示例 1:
#
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
#  示例 2:
#
#  输入: s = "rat", t = "car"
# 输出: false
#
#  说明:
# 你可以假设字符串只包含小写字母。
#
#  进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#  Related Topics 排序 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 字母异位词，排序之后应该一样
    # 复杂度分析：
    #     时间复杂度：O(n log n)
    #     空间复杂度：
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return sorted([c for c in s]) == sorted([c for c in t])

    # 使用map记录每个字符的出现的次数，遍历s的时候+1，遍历t的时候-1
    # 如果出现一个不为0的字符，那说明不是异位词
    # 复杂度分析：
    #     时间复杂度：O(n)
    #     空间复杂度：O(1)，字符数有限，故是常数的
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        c_map = {}
        for c1, c2 in zip(s, t):
            c_map[c1] = c_map.get(c1, 0) + 1
            c_map[c2] = c_map.get(c2, 0) - 1

        for c, n in c_map.items():
            if n != 0:
                return False

        return True

# leetcode submit region end(Prohibit modification and deletion)
