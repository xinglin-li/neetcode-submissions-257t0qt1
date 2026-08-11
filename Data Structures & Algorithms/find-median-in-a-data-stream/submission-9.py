class MedianFinder:

    def __init__(self):
        self.small = [] # 大顶堆
        self.large = [] # 小顶堆

    def addNum(self, num: int) -> None:
        # 1. 默认先压入小顶
        heapq.heappush(self.small, -num)
        # 2. 保证small的最大值 <= large的最小值
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # 3. 维护两堆的大小平衡, small最多比large多一个元素
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
        
        