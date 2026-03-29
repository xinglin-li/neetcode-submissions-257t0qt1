# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return []
        if not l1:
            return l2
        if not l2:
            return l1

        carry = 0
        dummy = ListNode()
        dummy.next = l1
        prev = dummy
        p1, p2 = l1, l2
        while p1 and p2:
            s = p1.val + p2.val + carry
            carry = s // 10
            p1.val = s % 10
            p1 = p1.next
            p2 = p2.next
            prev = prev.next
        
        while p1:
            s = p1.val + carry
            carry = s // 10
            p1.val = s % 10
            p1 = p1.next
            prev = prev.next

        while p2:            
            s = p2.val + carry
            carry = s // 10
            prev.next = ListNode(s % 10)
            p2 = p2.next
            prev = prev.next
        if carry:
            prev.next = ListNode(1)
        return dummy.next

