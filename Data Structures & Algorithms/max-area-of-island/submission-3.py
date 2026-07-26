class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            # 图的题一定要记得对路径做标记
            grid[r][c] = 0
            area = 1
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)
            return area
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i,j))
        
        return ans