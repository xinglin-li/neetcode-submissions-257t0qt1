# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            s = v1 + v2 + carry
            carry = s // 10
            digit = s % 10

            cur.next = ListNode(digit)
            cur = cur.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1

        head = ListNode(0)
        cur = head
        p1 = l1
        p2 = l2
        add_digit=0
        while p1 or p2:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0
            cur_digit = (p1_val + p2_val)%10
            one_more = (cur_digit+add_digit)//10
            cur_digit = (cur_digit+add_digit)%10
            cur.next = ListNode(cur_digit)
            cur = cur.next
            add_digit = one_more +  (p1_val + p2_val)//10
            p1 = p1.next if p1 else p1
            p2 = p2.next if p2 else p2
        if add_digit == 1:
            cur.next = ListNode(1)
        return head.next
"""