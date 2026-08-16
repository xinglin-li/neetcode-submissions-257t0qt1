class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        # 优先队列：(将该点加入生成树的最小边权, 点的索引)
        pq = [(0, 0)]  # 从第 0 个点开始构建最小生成树 (Prim 算法)
        total_cost = 0
        
        while len(visited) < n:
            cost, u = heapq.heappop(pq)
            
            # 已经在最小生成树中的点跳过
            if u in visited:
                continue
                
            visited.add(u)
            total_cost += cost
            
            # 计算当前点到所有未访问点的曼哈顿距离并入堆
            x1, y1 = points[u]
            for v in range(n):
                if v not in visited:
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(pq, (dist, v))
                    
        return total_cost