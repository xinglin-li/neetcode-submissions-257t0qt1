# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists and return it as one sorted list.
        Uses a min-heap to always pick the smallest head among the lists.
        """
        import heapq

        heap = []
        for i, node in enumerate(lists):
            heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        cur = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
        