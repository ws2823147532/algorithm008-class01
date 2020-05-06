# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
#
#  假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
#
#  例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
#
#  与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
#
#  现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变
# 化次数。如果无法实现目标变化，请返回 -1。
#
#  注意:
#
#
#  起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
#  所有的目标基因序列必须是合法的。
#  假定起始基因序列与目标基因序列是不一样的。
#
#
#  示例 1:
#
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# 返回值: 1
#
#
#  示例 2:
#
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# 返回值: 2
#
#
#  示例 3:
#
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# 返回值: 3
#
#


# leetcode submit region begin(Prohibit modification and deletion)
# 思路：
# BFS-广度优先遍历
#     从start开始，每次改变其中一个字符，如果存在于bank，那么假如队列，如果得到了end，返回改变次数
from typing import List


class Solution:
    def minMutation1(self, start: str, end: str, bank: List[str]) -> int:
        if not bank: return -1
        bank = set(bank)
        if end not in bank or not start or not end: return -1
        import collections
        q = collections.deque()
        q.append(start)

        four = {'A': ['C', 'G', 'T'], 'C': ['A', 'G', 'T'], 'G': ['A', 'C', 'T'], 'T': ['A', 'C', 'G']}
        res = 0
        while q:
            res += 1
            for j in range(len(q)):
                curr = q.pop()
                for i in range(len(curr)):
                    three = four[curr[i]]
                    for c in three:
                        tmp = curr[:i] + c + curr[i + 1:]
                        if tmp == end:
                            return res
                        elif tmp in bank:
                            q.append(tmp)
                            bank.remove(tmp)
        return -1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank: return -1
        bank = set(bank)
        if end not in bank or not start or not end: return -1

        four = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
        q = [(start, 0)]
        l = len(start)
        while q:
            curr, level = q.pop(0)
            if curr == end: return level
            for i in range(l):
                three = four[curr[i]]
                for c in three:
                    tmp = curr[:i] + c + curr[i + 1:]
                    if tmp in bank:
                        q.append((tmp, level + 1))
                        bank.remove(tmp)
        return -1


# leetcode submit region end(Prohibit modification and deletion)
res = Solution().minMutation("AACCGGTT",
                             "AAACGGTA",
                             ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"])
print(res)
