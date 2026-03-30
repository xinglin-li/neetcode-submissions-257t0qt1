class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        if not grid or not grid[0]:
            return 
        INF = 2147483647
        q = deque()
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r,c))
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        while q:
            r,c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr > m-1 or nc < 0 or nc > n-1 or grid[nr][nc] != INF:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr,nc))

