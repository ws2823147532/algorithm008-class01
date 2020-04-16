# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  示例： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 方式一、迭代：加一个头结点的哨兵，可以优化逻辑
# 方式二、递归：递归公式：
#   if l1.val<=l2.val: l1.next = merge(l1.next, l2)
#   if l1.val>l2.val: l2.next = merge(l1, l2.next)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 添加一个哨兵
        curr = pre_head = ListNode(0)
        pre_head.next = l1
        while l1 and l2:
            if l1.val <= l2.val:
                curr = l1
                l1 = l1.next
            else:
                tmp = l2.next
                l2.next = curr.next
                curr.next = l2
                curr = l2
                l2 = tmp

        if l2:
            curr.next = l2

        return pre_head.next


# leetcode submit region end(Prohibit modification and deletion)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

node11 = ListNode(1)
node22 = ListNode(3)
node33 = ListNode(4)
node11.next = node22
node22.next = node33
res = Solution().mergeTwoLists(node1, node11)
print(res)
