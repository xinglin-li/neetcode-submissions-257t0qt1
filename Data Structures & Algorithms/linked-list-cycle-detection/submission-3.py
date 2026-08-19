# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        # 快指针每次走两步，需保证 fast 与 fast.next 非空
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 快慢指针相遇，说明存在环
            if slow == fast:
                return True
        return False