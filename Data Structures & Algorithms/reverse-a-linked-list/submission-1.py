# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list.
        
        Args:
            head: ListNode - The head of the linked list
            
        Returns:
            ListNode - The new head of the reversed linked list
        """
        # Initialize pointers
        prev = None
        current = head
        
        # Iterate through the list
        while current:
            # Store the next node before we lose the reference
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move pointers forward
            prev = current
            current = next_node
        
        # prev is now the new head of the reversed list
        return prev