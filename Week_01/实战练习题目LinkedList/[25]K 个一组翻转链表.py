# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
#  k 是一个正整数，它的值小于或等于链表的长度。
#
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#
#
#  示例：
#
#  给你这个链表：1->2->3->4->5
#
#  当 k = 2 时，应当返回: 2->1->4->3->5
#
#  当 k = 3 时，应当返回: 3->2->1->4->5
#
#
#
#  说明：
#
#
#  你的算法只能使用常数的额外空间。
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        res = [self.val]
        tmp_node = self.next
        while tmp_node:
            res.append(tmp_node.val)
            tmp_node = tmp_node.next
        return ''.join([str(i) for i in res])


def next_node(head, k):
    i = 0
    while head and i < k:
        head = head.next
        i += 1

    return head, i


def reverse_list(head, k):
    i = 0
    first = last = head
    prev = None
    while i < k:
        tmp = first.next
        first.next = prev
        prev = first
        first = tmp
        i += 1

    return prev, last


class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 递归的结束条件：如果当前的链表已经不满k个元素，直接返回
        node, list_length = next_node(head, k)

        if not node and list_length < k or list_length < k: return head

        # 假设当前的k元组已经反转完，递归地去反转下一个k元组，并且返回下一个k元组的第一个节点
        ret = self.reverseKGroup(node, k) if node else None

        # 反转当前的k元组 等价于 反转链表(遍历、递归、使用栈)
        # 最终将最后一个节点的next指向ret
        # O(n)
        first, last = reverse_list(head, k)
        last.next = ret
        return first


# leetcode submit region end(Prohibit modification and deletion)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# f, l = reverse_list(n1, k=5)
# print(f.val, l.val)

# res, le = next_node(n1, 5)
# print(res, le)

res = Solution().reverseKGroup(n1, 2)
print(res)
