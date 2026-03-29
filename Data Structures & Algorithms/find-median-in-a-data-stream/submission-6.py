import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max-heap by pushing negatives
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # 先放到 small（最大堆）
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # 重新平衡：small 至多比 large 多 1 个
        if len(self.small) < len(self.large):
            # large -> small
            heapq.heappush(self.small, -heapq.heappop(self.large))
        elif len(self.small) - len(self.large) > 1:
            # small -> large
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # 保障顺序不变式（通常上面逻辑已满足，以下仅在极端插入顺序时兜底）
        if self.large and -self.small[0] > self.large[0]:
            # 交换堆顶以修正顺序
            a = -heapq.heappop(self.small)
            b = heapq.heappop(self.large)
            heapq.heappush(self.small, -b)
            heapq.heappush(self.large, a)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

        
        