# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # 让 fast 比 slow 提前 n 步
        for _ in range(n):
            fast = fast.next

        # 保证 slow 最终停在待删除节点的前一个节点
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 删除倒数第 n 个节点
        slow.next = slow.next.next

        return dummy.next