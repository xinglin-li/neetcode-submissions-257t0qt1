# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # 暂存原 next
            curr.next = prev     # 指针反转
            prev = curr          # 滚动 prev
            curr = nxt           # 滚动 curr

        return prev