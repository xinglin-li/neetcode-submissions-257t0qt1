class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        maxheap = []
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(maxheap, -projects[i][1])
                i += 1
            if maxheap:
                profit = -heapq.heappop(maxheap)
                w += profit
            else:
                break
        return w

