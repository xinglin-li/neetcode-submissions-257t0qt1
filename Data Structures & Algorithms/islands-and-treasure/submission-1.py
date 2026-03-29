class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        m, n = len(grid), len(grid[0])
        q = deque()

        # 1. 把所有 treasure (0) 放入队列（多源 BFS）
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        # 2. BFS 扩散，更新 land
        while q:
            i, j = q.popleft()
            for di, dj in dirs:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 2147483647:
                    grid[x][y] = grid[i][j] + 1
                    q.append((x, y))


        
