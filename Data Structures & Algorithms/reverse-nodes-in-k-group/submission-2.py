# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            # 1. 找下一段的末尾（第 k 个）
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            groupNext = kth.next

            # 2. 反转 groupPrev.next 到 kth 这段
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 3. 拼接
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp