# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        # --- 第一步：找到中点并断开 ---
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None
        l1 = head

        # --- 第二步：反转后半部分链表 ---
        prev = None
        curr = l2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        l2 = prev
        
        # --- 第三步：交错合并 ---
        while l1 and l2:
            l1_nxt = l1.next
            l2_nxt = l2.next
            l1.next = l2
            if l1_nxt is None:
                break
            l2.next = l1_nxt
            l1 = l1_nxt
            l2 = l2_nxt