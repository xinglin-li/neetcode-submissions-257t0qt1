class StockSpanner:
    # Monotonic stack
    # 维护一个单调递减栈（Monotonic Decreasing Stack）
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # 当栈顶的价格 <= 当前价格 → 被“压制”，可以直接合并区间
        # You will never need (p,s) pair once you pop it
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            p,s = self.stack.pop()
            span += s
        self.stack.append((price,span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)