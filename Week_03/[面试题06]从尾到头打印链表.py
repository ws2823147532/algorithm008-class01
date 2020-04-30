# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
#
#
#
#  示例 1：
#
#  输入：head = [1,3,2]
# 输出：[2,3,1]
#
#
#
#  限制：
#
#  0 <= 链表长度 <= 10000
#


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List


class Solution:
    def reversePrint1(self, head: ListNode) -> List[int]:
        if not head: return []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return [num for num in reversed(res)]

    def reversePrint(self, head: ListNode) -> List[int]:
        if not head: return []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        l = len(res)
        for i in range(l // 2):
            res[i], res[l - i - 1] = res[l - i - 1], res[i]

        return res

# leetcode submit region end(Prohibit modification and deletion)
