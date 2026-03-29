# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders the list in-place to L0→Ln→L1→Ln-1→L2→Ln-2→...

        Algorithm:
        1. Find the middle with slow/fast pointers.
        2. Reverse the second half.
        3. Merge the two halves alternating nodes.

        Args:
            head: ListNode | None

        Returns:
            None (modify list in-place)
        """
        if not head or not head.next:
            return

        # 1. Find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is at middle (for odd n it's the middle, for even it's the start of second half)

        # 2. Reverse second half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev is head of reversed second half

        # 3. Merge first half and reversed second half
        first = head
        second = prev
        while second and first:
            # Save next pointers
            f_next = first.next
            s_next = second.next

            # Link
            first.next = second
            # If f_next is the same node as second (odd length case), break
            if f_next is second:
                break
            second.next = f_next

            # Move pointers
            first = f_next
            second = s_next