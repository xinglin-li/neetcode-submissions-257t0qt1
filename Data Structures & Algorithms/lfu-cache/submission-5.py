class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.freq = 1  # 新节点初始频率为 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """带伪头尾节点的标准双向链表"""
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    def append_to_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self._size += 1

    def remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

    def remove_tail(self) -> Node:
        if self._size == 0:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node

    def __len__(self):
        return self._size


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}   # key -> Node
        self.freq_map = {}  # freq -> DoublyLinkedList
        self.min_freq = 0   # 维护全局最小频率

    def _increase_freq(self, node: Node):
        """核心辅助函数：提高某个节点的频率计数，并平移到新的频率链表中"""
        old_freq = node.freq
        
        # 1. 从旧频率链表中移除
        self.freq_map[old_freq].remove_node(node)
        
        # 2. 如果旧链表空了，且刚好是当前的最小频率，更新 min_freq
        if len(self.freq_map[old_freq]) == 0 and old_freq == self.min_freq:
            self.min_freq += 1
            
        # 3. 更新节点频率并移入新链表
        node.freq += 1
        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = DoublyLinkedList()
        self.freq_map[node.freq].append_to_head(node)

    def get(self, key: int) -> int:
        if self.capacity == 0 or key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._increase_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # 情况 1：Key 已存在，更新值并增加频率
        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self._increase_freq(node)
            return

        # 情况 2：Key 不存在，需要插入新节点
        # 如果缓存满了，先淘汰
        if len(self.key_map) == self.capacity:
            # 找到当前最小频率的链表，淘汰尾部节点
            min_freq_list = self.freq_map[self.min_freq]
            deleted_node = min_freq_list.remove_tail()
            del self.key_map[deleted_node.key]

        # 插入新节点，新节点初始频率必定为 1
        new_node = Node(key, value)
        self.key_map[key] = new_node
        self.min_freq = 1  # 新来的人频率是1，所以全局最小频率被重置回 1
        
        if 1 not in self.freq_map:
            self.freq_map[1] = DoublyLinkedList()
        self.freq_map[1].append_to_head(new_node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)