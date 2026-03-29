class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or r > m-1 or c < 0 or c > n-1 or grid[r][c] == 0:
                return 0 
            grid[r][c] = 0
            area = 1
            for dr, dc in [(1,0), (0,1), (-1,0), (0, -1)]:
                nr,nc = r + dr, c + dc
                area += dfs(nr,nc)
            return area
        
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r,c))
        return ans