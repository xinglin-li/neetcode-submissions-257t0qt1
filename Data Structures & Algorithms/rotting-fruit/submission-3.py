class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        m, n = len(grid), len(grid[0])
        q = deque()
        
        fresh = 0
        
        # 1. 把所有 rotten oranges 加入队列
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        t = 0
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        
        # 2. BFS 层序
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        q.append((x, y))
            if q:
                t += 1
        
        return t if fresh == 0 else -1
"""
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
"""