class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> ListNode
        
        # 初始化伪头部和伪尾部节点
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            
            # 如果超出容量，移除最久未使用的节点（尾部的前一个节点）
            if len(self.cache) > self.capacity:
                removed_node = self._remove_tail()
                del self.cache[removed_node.key]

    # --- 辅助双向链表操作函数 ---
    
    def _add_to_head(self, node: ListNode):
        """将新节点插入到伪头部后面"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: ListNode):
        """将当前节点从双向链表中拆离"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node: ListNode):
        """移动现有节点到头部 = 先拆出来 + 再插到头部"""
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self) -> ListNode:
        """淘汰最久未使用的节点，并返回它（以便在哈希表中同步删除键）"""
        node = self.tail.prev
        self._remove_node(node)
        return node
        
