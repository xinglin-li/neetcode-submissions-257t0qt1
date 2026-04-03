class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        # 优先队列存放元组：(当前路径的最大 effort, r, c)
        # 最小堆保证每次弹出的都是当前已知 effort 最小的节点
        pq = [(0, 0, 0)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        while pq:
            current_effort, r, c = heapq.heappop(pq)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            
            # 优化：一旦弹出了终点，说明找到了最优解，直接返回
            if r == rows - 1 and c == cols - 1:
                return current_effort
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    # 计算当前走这一步的“边权”
                    edge_weight = abs(heights[r][c] - heights[nr][nc])
                    
                    # 走到邻居节点的新瓶颈：是“之前的路径瓶颈”和“当前边权”中的最大值
                    new_effort = max(current_effort, edge_weight)
                    
                    heapq.heappush(pq, (new_effort, nr, nc))
                        
        return 0




