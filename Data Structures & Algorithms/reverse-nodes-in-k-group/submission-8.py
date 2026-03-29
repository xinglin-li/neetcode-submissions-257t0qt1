# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def find_kth(node,k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node
        
        dummy = ListNode(0, head)
        preGroup = dummy
        while True:
            kth = find_kth(preGroup, k)
            if not kth:
                break
            postGroup = kth.next
            prev = postGroup
            cur = preGroup.next

            while cur != postGroup:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = preGroup.next
            preGroup.next = kth
            preGroup = tmp
        return dummy.next 
