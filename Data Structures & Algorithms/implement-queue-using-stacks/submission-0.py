class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        res = self.out_stack.pop()
        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())
        return res

    def peek(self) -> int:
        return self.in_stack[0]

    def empty(self) -> bool:
        return len(self.in_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()