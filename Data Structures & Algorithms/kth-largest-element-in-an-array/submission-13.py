class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                # pop掉小的，剩下的就是大的
                heapq.heappop(heap)
        return heap[0]
