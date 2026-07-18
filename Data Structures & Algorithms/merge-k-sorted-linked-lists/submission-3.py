# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 创建一个虚拟头节点，方便串联结果
        dummy = ListNode(0)
        curr = dummy
        
        heap = []
        count = 0  # 计数器，用于解决 Python 的对象比较冲突大坑
        
        # 1. 将所有链表的非空头节点存入堆中
        for head in lists:
            if head:
                # 元组格式: (节点值, 唯一计数器, 节点对象)
                heapq.heappush(heap, (head.val, count, head))
                count += 1
                
        # 2. 依次弹出最小节点并进行拼接
        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node  # 接上当前最小节点
            curr = curr.next  # 指针后移
            
            # 3. 如果该节点后续还有节点，将下一个节点推入堆中
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
                count += 1
                
        return dummy.next
        