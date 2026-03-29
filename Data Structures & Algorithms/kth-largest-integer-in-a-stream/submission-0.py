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
