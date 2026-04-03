class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        # 记录从起点到达每个节点所需的最小 effort（最大瓶颈）
        # 初始化为无穷大
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        
        # 优先队列存放元组：(当前路径的最大 effort, r, c)
        # 最小堆保证每次弹出的都是当前已知 effort 最小的节点
        pq = [(0, 0, 0)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            current_effort, r, c = heapq.heappop(pq)
            
            # 优化：一旦弹出了终点，说明找到了最优解，直接返回
            if r == rows - 1 and c == cols - 1:
                return current_effort
            
            # 剪枝：如果弹出的状态是一个过时的状态（比当前记录的还要差），直接跳过
            if current_effort > efforts[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # 计算当前走这一步的“边权”
                    edge_weight = abs(heights[r][c] - heights[nr][nc])
                    
                    # 走到邻居节点的新瓶颈：是“之前的路径瓶颈”和“当前边权”中的最大值
                    new_effort = max(current_effort, edge_weight)
                    
                    # 松弛操作：如果找到了一条瓶颈更小的路径，更新并入队
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
                        
        return 0




