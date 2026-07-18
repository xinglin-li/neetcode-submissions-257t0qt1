class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0]*k
        self.head = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        target_idx = (self.head + self.size) % self.capacity
        self.queue[target_idx] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        rear_idx = (self.head + self.size - 1) % self.capacity
        return self.queue[rear_idx]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()