# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
#  说明：不允许修改给定的链表。
#
#
#
#  示例 1：
#
#  输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#
#
#  示例 2：
#
#  输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#
#
#  示例 3：
#
#  输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
#
#
#
#
#
#
#  进阶：
# 你是否可以不用额外空间解决此题？
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __str__(self):
    #     return str(self.val)


# 思路一：使用set储存遍历过的节点
# 思路二：快慢指针，两次循环
class Solution:
    def detectCycle1(self, head: ListNode) -> ListNode:
        tmp = set()

        while head:
            if head in tmp:
                return head
            tmp.add(head)
            head = head.next

        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return head

        slow, fast = head, head.next
        meet = None
        # find the meeting node
        while fast and fast.next:
            # fast is the meeting node
            if slow == fast:
                meet = slow
                break

            slow = slow.next
            fast = fast.next.next

        if not meet: return None

        # find the first cycle node
        slow, fast = head, meet.next
        while fast:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next

        return None


# leetcode submit region end(Prohibit modification and deletion)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
# n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2
# n4.next = n5
res = Solution().detectCycle(n1)
print(res)
