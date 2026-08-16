class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        # dist[r][c] 记录从起点到达 (r, c) 路径上的最小体力消耗（即路径上的最大相邻高差）
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        
        # 优先队列维护三元组：(当前路径的最大高度差, r, c)
        pq = [(0, 0, 0)]
        
        while pq:
            effort, r, c = heapq.heappop(pq)
            
            # Dijkstra 贪心性质：首次弹出终点时即为全局最优解
            if r == rows - 1 and c == cols - 1:
                return effort
            
            # 剪枝：若当前弹出的 effort 大于已记录的最优值，说明是冗余状态，直接跳过
            if effort > dist[r][c]:
                continue
                
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # 转移逻辑：到达新格子的体力消耗为 max(历史最大落差, 跨越当前格子的落差)
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
                        
        return 0