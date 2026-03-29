class KthLargest:
    # smarter way: you only need to maintain a heap with the largest k elements
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # 让 heap 只保留 k 个最大元素
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # 维持长度 k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # heap[0] 就是第 k 大元素
        return self.heap[0]

"""
# It passed, but we have a cleverer solution
class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        nums = [-i for i in nums]
        self.k = k
        self.heap = nums
        heapq.heapify(nums)

    def _heapsort(self, heap):
        res = []
        while heap:
            min_val = heapq.heappop(heap)
            res.append(min_val)
        return res

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        self.heap = self._heapsort(self.heap)
        return -self.heap[self.k-1]
"""
