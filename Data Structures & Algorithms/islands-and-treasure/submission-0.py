class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        m, n = len(grid), len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        while q:
            i,j = q.popleft()
            for dx,dy in dirs:
                x = i + dx
                y = j + dy

                if 0 <= x <= m-1 and 0 <= y <= n-1 and grid[x][y] == 2147483647:
                    grid[x][y] = grid[i][j] + 1
                    q.append((x,y))


        
