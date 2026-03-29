# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Euclid’s algorithm manually to find GCD as a practice later
        from math import gcd
        dummy = ListNode()
        dummy.next = head
        cur = nxt = head
        while cur.next:
            mid = gcd(cur.val, cur.next.val)
            nxt = cur.next
            cur.next = ListNode(mid)
            cur.next.next = nxt
            cur = nxt
        return dummy.next