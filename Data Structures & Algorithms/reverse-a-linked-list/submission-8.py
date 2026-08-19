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
            nxt = curr.next     # 1. 暂存下一个节点
            curr.next = prev    # 2. 改变指针朝向
            prev = curr         # 3. prev 前移
            curr = nxt          # 4. curr 前移
            
        return prev
