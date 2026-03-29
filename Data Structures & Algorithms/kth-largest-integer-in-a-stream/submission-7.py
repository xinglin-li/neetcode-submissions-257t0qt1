class KthLargest:
    # smarter way: you only need to maintain a heap with the largest k elements
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.heap = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
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
