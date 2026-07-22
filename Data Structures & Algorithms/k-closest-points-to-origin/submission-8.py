class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for pt in points:
            x, y = pt
            heapq.heappush(heap, ((x**2 + y**2), pt))
        
        res = []
        for _ in range(k):
            _, pt = heapq.heappop(heap)
            res.append(pt)
        
        return res
