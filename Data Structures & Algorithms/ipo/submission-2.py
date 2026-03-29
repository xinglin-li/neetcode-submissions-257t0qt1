class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        maxheap = []
        i = 0
        
        for _ in range(k):
            # push all projects whose required capital <= current capital w
            while i < len(projects) and projects[i][0] <= w:
                # store negative profit because heapq is min-heap by default
                heapq.heappush(maxheap, -projects[i][1])
                i += 1
            
            # no available project?
            if not maxheap:
                break
            
            # pick best project and increase capital
            w += -heapq.heappop(maxheap)

        return w

