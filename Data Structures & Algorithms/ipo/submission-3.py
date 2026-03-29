class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq
        projects = sorted(zip(capital, profits))
        maxHeap = []
        i = 0
        n = len(projects)

        for _ in range(k):

            while i < n and projects[i][0] <= w:
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1
            if not maxHeap:
                break
            w -= heapq.heappop(maxHeap)
        
        return w
