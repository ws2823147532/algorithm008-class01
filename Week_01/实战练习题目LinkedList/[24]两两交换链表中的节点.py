# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
#  示例:
#
#  给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val


class Solution:
    # 无哨兵
    def swapPairs1(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        res, first, second = head.next, head, head.next
        while first and second:
            tmp = second.next
            second.next = first
            first.next = tmp.next if tmp and tmp.next else tmp
            first = tmp
            second = tmp.next if tmp else None

        return res

    # 哨兵:添加哨兵的目的是优化边界的操作。此处是充当了head的前驱结点
    def swapPairs3(self, head: ListNode) -> ListNode:
        if not head: return head
        sentinel = ListNode(-1)
        sentinel.next = head

        prev = sentinel

        first = head
        while first and first.next:
            second = first.next

            # swap，注意swap的顺序，否则
            prev.next = second
            first.next = second.next
            second.next = first

            # 初始化下一次循环的swap
            prev = first
            first = prev.next

        return sentinel.next

    # 使用栈操作：
    # 将2个2个的元素压入栈中，如果遇到第一个元素或者第二个元素为空 出栈
    # 否则，把出栈的两个元素swap一次
    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        res = []
        # 入栈 O(n)
        while head and head.next:
            res.append((head, head.next))
            head = head.next.next

        tail = head

        # 出栈：O(n)
        while len(res) > 0:
            pair = res.pop()
            pair[1].next = pair[0]
            pair[0].next = tail

            tail = pair[1]

        return tail

    # 递归：
    # 原理和使用栈的时候是一样的
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        ret = self.swapPairs(head.next.next)

        head.next.next = head
        tmp = head.next
        head.next = ret

        return tmp


# leetcode submit region end(Prohibit modification and deletion)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
# n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
# n4.next = n5
res = Solution().swapPairs(n1)
print(res.val)
