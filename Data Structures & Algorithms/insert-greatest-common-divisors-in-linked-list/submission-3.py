# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            c = math.gcd(cur.val, cur.next.val)
            nxt = cur.next
            cur.next = ListNode(c, nxt)
            cur = nxt
        
        return head