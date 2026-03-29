class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: 
                    q.append((i,j))
        
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        t = 0
        q_next = deque()
        while q:
            i,j = q.popleft()
            for dx,dy in dirs:
                x = i + dx
                y = j + dy
                if 0 <= x <= m-1 and 0 <= y <= n-1 and grid[x][y] == 1:
                    grid[x][y] = 2
                    q_next.append((x,y))
            if not q and q_next:
                q = q_next
                q_next = deque()
                t += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    return -1
        return t