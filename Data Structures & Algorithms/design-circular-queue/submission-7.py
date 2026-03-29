class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k       # 固定长度数组
        self.size = 0          # 当前元素数量
        self.k = k             # 容量
        self.head = 0          # 队头指针
        self.tail = 0         # 队尾指针（初始化为 0). tail 永远指向下一次 enqueue 的位置, 而不是最后一个元素。

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1)%self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1)%self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.tail-1)%self.k]


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()