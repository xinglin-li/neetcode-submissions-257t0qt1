# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1) Find the kth node.
        # 2) Reverse this part.
        # 3) Connect it to original LinkedList
        def find_kth(node, k):
            node
            while node and k > 0:
                node = node.next
                k -= 1
            return node
        
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy
        while True:
            kth = find_kth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev = groupNext
            cur = groupPrev.next

            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next