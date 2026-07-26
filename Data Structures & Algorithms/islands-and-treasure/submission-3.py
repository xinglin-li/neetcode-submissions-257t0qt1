class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi-source BFS, start form all treasures
        if not grid or not grid[0]:
            return None
        m, n = len(grid), len(grid[0])
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r,c))
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] != 2147483647:
                    continue
                q.append((nr,nc))
                grid[nr][nc] = grid[r][c] + 1
        
