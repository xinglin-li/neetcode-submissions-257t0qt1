# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        start = head
        then = head.next
        while start.next:
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then= start.next
        return dummy.next