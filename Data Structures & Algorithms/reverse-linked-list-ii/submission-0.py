# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        # 1. 让 pre 移动到 left 节点的前一个节点
        for _ in range(left - 1):
            pre = pre.next

        # start 是待反转区间的第一个节点
        # then 是 start 后面的节点
        start = pre.next
        then = start.next

        # 2. 头插法反转 left..right 区间
        for _ in range(right - left):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next

        return dummy.next
