class MedianFinder:
    def __init__(self):
        # small 是最大堆（存储较小的一半元素，Python 存负数值）
        # large 是最小堆（存储较大的一半元素）
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # 1. 默认先放进 small（最大堆）
        heapq.heappush(self.small, -num)
        
        # 2. 确保 small 中的最大值 <= large 中的最小值
        # 弹出 small 的堆顶（即最大值）放入 large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # 3. 维护两堆的数量平衡（保持 len(small) >= len(large)）
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # 如果总数为奇数，small 比 large 多一个元素，中位数就是 small 的堆顶
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        # 如果总数为偶数，取两堆堆顶的平均值
        return (-self.small[0] + self.large[0]) / 2.0
        
        