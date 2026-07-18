# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy  # 每组翻转前，该组前一个节点
        
        while True:
            # 1. 检查剩余节点是否满足 k 个
            kth_node = group_prev
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next  # 不足 k 个，直接返回结果
            
            # 记录下一组的开始节点和当前组的开始节点
            next_group_head = kth_node.next
            curr = group_prev.next
            
            # 2. 局部翻转当前组的 k 个节点（标准的双指针翻转）
            prev = next_group_head  # 让翻转后的尾节点直接连到下一组的头上
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            # 3. 将上一组的尾部与当前翻转后的头部（即原第 k 个节点）连起来
            # 注意：此时这组原本的第一个节点变成了尾节点
            temp = group_prev.next 
            group_prev.next = kth_node
            
            # 4. 指针复位，group_prev 移到当前组的尾部，为下一轮做准备
            group_prev = temp
