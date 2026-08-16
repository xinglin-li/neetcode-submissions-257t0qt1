class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            # 越界或者是水域，停止递归
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return
            # 淹没当前陆地，避免重复访问
            grid[r][c] = "0"
            # 递归上下左右四个方向
            for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j) # 将该岛屿的所有陆地全部“淹没”
        
        return ans


