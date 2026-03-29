# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Euclid’s algorithm manually to find GCD as a practice later
        from math import gcd
        def euclid_alg(a,b):
            while b:
                a,b = b, a%b
            return a

        cur = head
        while cur and cur.next:
            g = euclid_alg(cur.val, cur.next.val)
            node = ListNode(g, cur.next)
            cur.next = node
            cur = node.next   # move to the next original node
        return head