# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
#  示例:
#
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
#  说明：
#
#
#  所有输入均为小写字母。
#  不考虑答案输出的顺序。
#
#  Related Topics 哈希表 字符串


# leetcode submit region begin(Prohibit modification and deletion)
# 思路：
#     长度一样的放一起，然后找字母异位词
import collections


class Solution:

    # 异位词 排序之后应该是一样的
    def groupAnagrams2(self, strs):
        if not strs: return []
        map = collections.defaultdict(list)
        for s in strs:
            map[tuple(sorted(s))].append(s)

        return list(map.values())

    # 使用字符计数
    def groupAnagrams(self, strs):
        if not strs: return []

        map = collections.defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            map[tuple(cnt)].append(s)
        return list(map.values())


# leetcode submit region end(Prohibit modification and deletion)


res = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)
