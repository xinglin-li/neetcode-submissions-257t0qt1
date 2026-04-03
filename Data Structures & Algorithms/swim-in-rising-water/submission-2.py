class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # transfer the minimum time question to "find the path to destination with minimum max(heights of path)". 
        import heapq
        m, n = len(grid), len(grid[0])
        pq = [(grid[0][0], 0, 0)] # cost, r, c
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = {(0,0)}
        while pq:
            cost, r, c = heapq.heappop(pq)
            if r == m - 1 and c == n - 1:
                return cost
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited:
                    height = grid[nr][nc]
                    max_height = max(cost, height)
                    visited.add((nr,nc))
                    heapq.heappush(pq, (max_height, nr, nc))