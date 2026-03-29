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
            heapq.heappush(heap,(node.val, i, node))
        
        dummy = ListNode()
        curr = dummy
        while heap:
            _, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                # Note here is node.next!!!
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next

        