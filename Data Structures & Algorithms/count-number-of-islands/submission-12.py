class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r,c):
            if r < 0 or r > m - 1 or c < 0 or c > n - 1 or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    ans += 1
                    dfs(r,c)
        return ans