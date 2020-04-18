# 反转一个单链表。
#
#  示例:
#
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
#  进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 链表的操作十分不熟练
class Solution:
    # 遍历
    def reverseList1(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    # 利用栈
    def reverseList2(self, head: ListNode) -> ListNode:
        if not head: return
        res = []
        while head:
            res.append(head)
            head = head.next

        head = tmp = res.pop()
        while len(res) > 0:
            tmp.next = res.pop()
            tmp = tmp.next
        tmp.next = None
        return head

    # 递归
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        ret = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        return ret


# leetcode submit region end(Prohibit modification and deletion)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
res = Solution().reverseList(n1)
print(res.val)
