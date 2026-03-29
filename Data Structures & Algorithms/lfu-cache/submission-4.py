class Node:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.freq = 1 #something new
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def add_to_front(self, node: None) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def remove_node(self, node: None) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
    
    def remove_last(self) -> Node:
        if self.size == 0:
            return None
        last = self.tail.prev
        self.remove_node(last)
        return last

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_list = {} # values is doubly LinkedList

    def _update_freq(self, node: None) -> None:
        freq = node.freq
        self.freq_to_list[freq].remove_node(node)

        if freq == self.min_freq and self.freq_to_list[freq].size == 0:
            self.min_freq += 1
        
        node.freq += 1
        new_freq = node.freq

        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DoublyLinkedList()
        self.freq_to_list[new_freq].add_to_front(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self._update_freq(node)
        return node.val   

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self._update_freq(node)
            return
        
        if len(self.key_to_node) == self.capacity:
            lfu_list = self.freq_to_list[self.min_freq]
            node_to_remove = lfu_list.remove_last()
            del self.key_to_node[node_to_remove.key]
        
        new_node = Node(key, value)
        self.key_to_node[key] = new_node

        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()
        self.freq_to_list[1].add_to_front(new_node)
        self.min_freq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)