class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits), key=lambda x: x[0])

        max_heap = [] # 大顶堆, 存利润
        i = 0
        n = len(projects)

        for _ in range(k):
            # 将所有启动资本 <= w 的项目推入堆
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            # 若为空, 说明无法开启任何项目
            if not max_heap:
                break
            
            w -= heapq.heappop(max_heap)
        
        return w