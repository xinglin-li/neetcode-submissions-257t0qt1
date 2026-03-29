class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # priority queue, priority is distance.
        import heapq
        heap = []
        for point in points:
            x, y = point
            heapq.heappush(heap,((x**2+y**2),point))
        
        res = []
        for _ in range(k):
            _ , pt = heapq.heappop(heap)
            res.append(pt)
        
        return res