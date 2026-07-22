class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        i = 1
        while i < k:
            heapq.heappop(heap)
            i += 1
        return -heap[0]
