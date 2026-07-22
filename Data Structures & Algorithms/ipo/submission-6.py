class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 1. 将项目组合并按需要的启动资本 capital 升序排序
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        
        max_heap = []
        i = 0
        n = len(projects)
        
        # 最多选择 k 个项目
        for _ in range(k):
            # 将所有当前资本 w 能够启动的项目利润压入最大堆
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # 存负数模拟最大堆
                i += 1
                
            # 如果没有可以启动的项目，直接跳出
            if not max_heap:
                break
                
            # 贪心选择当前能获得的最大利润
            w += -heapq.heappop(max_heap)
            
        return w
