class Node:
    def __init__(self, key, value, freq = 1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def pop(self, node=None):
        if self.size == 0:
            return None
        if not node:
            node = self.head.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        if capacity == 0:
            return
        self.key_table = {}
        self.freq_table = {}
        self.minFreq = 0
    
    def _update(self, node):
        """Helper: move node from freq to freq+1 list."""
        freq = node.freq
        self.freq_table[freq].pop(node)
        if self.freq_table[freq].size == 0:
            if freq == self.minFreq:
                self.minFreq += 1

        node.freq += 1
        self.freq_table.setdefault(node.freq, DoublyLinkedList()).append(node)

    def get(self, key: int) -> int:
        if key not in self.key_table:
            return -1
        node = self.key_table[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.key_table:
            node = self.key_table[key]
            node.value = value
            self._update(node)
            return
        # capacity full → evict LFU
        if len(self.key_table) == self.cap:
            lfu_list = self.freq_table[self.minFreq]
            node_to_remove = lfu_list.pop()
            del self.key_table[node_to_remove.key]
        
        # insert new node with freq = 1
        new_node = Node(key, value)
        self.key_table[key] = new_node
        self.freq_table.setdefault(1, DoublyLinkedList()).append(new_node)
        self.minFreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)