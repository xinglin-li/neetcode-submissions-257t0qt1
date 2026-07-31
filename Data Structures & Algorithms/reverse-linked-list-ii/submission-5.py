# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # 1. 创建哨兵节点，统一处理包含头节点反转的情况
        dummy = ListNode(0, head)
        prev = dummy

        # 2. 将 prev 指针移动到 left 的前一个节点
        for _ in range(left - 1):
            prev = prev.next

        # 3. 头插法：在 [left, right] 区间内依次将节点拿到 prev 后面
        curr = prev.next
        for _ in range(right - left):
            nxt = curr.next # 锁定下一个目标
            curr.next = nxt.next # 孤立掉目标
            nxt.next = prev.next # 目标指向prev结点指向的东西
            prev.next = nxt # prev指向插进来的节点
        
        return dummy.next

