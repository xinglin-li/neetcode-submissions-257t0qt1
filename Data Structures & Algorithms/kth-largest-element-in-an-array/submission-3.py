class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap. nlogk
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            else:
                if x > heap[0]:
                    heapq.heapreplace(heap,x)
        return heap[0]