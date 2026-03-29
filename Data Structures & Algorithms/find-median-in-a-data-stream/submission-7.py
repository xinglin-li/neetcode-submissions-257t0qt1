import heapq

class MedianFinder:
    # two heaps. maxHeap and minHeap
    def __init__(self):
        self.small = [] # maxHeap
        self.large = [] # minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2
        else:
            return -self.small[0]
        