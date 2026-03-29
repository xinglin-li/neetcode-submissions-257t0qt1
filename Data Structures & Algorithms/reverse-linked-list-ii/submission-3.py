# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        # 1. move prev to node before left
        for _ in range(left-1):
            prev = prev.next
        
        curr = prev.next
        # 2. reverse [left, right], head insertion.
        for _ in range(right-left):
            temp = curr.next
            curr.next = temp.next # curr is always the last node, keep inserting nodes before it.
            temp.next = prev.next 
            prev.next = temp
        return dummy.next