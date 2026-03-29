# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []
        
        fast = head
        for _ in range(n):
            fast = fast.next
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        while fast:
            fast = fast.next
            cur = cur.next
            prev = prev.next
        
        nxt = cur.next
        prev.next = nxt
        return dummy.next
