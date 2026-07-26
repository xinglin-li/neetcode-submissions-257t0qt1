class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        
        return ans


