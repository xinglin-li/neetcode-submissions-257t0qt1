class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        import heapq
        
        rows, cols = len(heights), len(heights[0])
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        
        pq = [(0, 0, 0)]  # (effort, r, c)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            effort, r, c = heapq.heappop(pq)
            if r == rows - 1 and c == cols - 1:
                return effort
            if effort > efforts[r][c]:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    cost = abs(heights[nr][nc] - heights[r][c])
                    new_effort = max(effort, cost)
                    
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))

        return 0