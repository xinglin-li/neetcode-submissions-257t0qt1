class MedianFinder:
    # Two heaps
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        elif len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if self.large and -self.small[0] > self.large[0]:
            a = - heapq.heappop(self.small) 
            b = - heapq.heappop(self.large)
            heapq.heappush(self.small, b)
            heapq.heappush(self.large, a)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0])/2.0
        
        