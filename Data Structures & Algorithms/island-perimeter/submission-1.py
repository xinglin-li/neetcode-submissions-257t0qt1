class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        perimeter = 0
        
        def dfs(i, j):
            nonlocal perimeter
            visited[i][j] = True
            
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                
                # 1⃣ 越界 → 增加一条边
                if not (0 <= x < m and 0 <= y < n):
                    perimeter += 1
                    continue
                
                # 2⃣ 邻居是水 → 增加一条边
                if grid[x][y] == 0:
                    perimeter += 1
                    continue
                
                # 3⃣ 邻居是陆地 & 未访问 → DFS
                if not visited[x][y]:
                    dfs(x, y)
        
        # 找到第一个陆地，从它开始 DFS
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter
        
        return 0