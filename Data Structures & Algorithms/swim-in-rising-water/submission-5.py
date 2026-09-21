class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # transfer the minimum time question to "find the path to destination with minimum max(heights of path)". 
        m, n = len(grid), len(grid[0])
        min_heap = [(grid[0][0], 0, 0)]
        visited = set()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue

            if (r, c) == (m - 1, n - 1):
                return time
            
            visited.add((r,c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(min_heap, (new_time, nr, nc))
        return -1