from typing import List, Set, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r: int, c: int, seen: Set[Tuple[int,int]]):
            if (r, c) in seen:
                return
            seen.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, seen)

        pac, atl = set(), set()

        # 太平洋：上边、左边
        for c in range(n):
            dfs(0, c, pac)
        for r in range(m):
            dfs(r, 0, pac)

        # 大西洋：下边、右边
        for c in range(n):
            dfs(m - 1, c, atl)
        for r in range(m):
            dfs(r, n - 1, atl)

        return [[r, c] for (r, c) in pac & atl]

"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        ans = []
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def bfs(x,y,seen):
            if (x,y) in seen:
                return
            seen.add((x,y))
            q = deque([(x,y)])
            while q:
                x,y = q.popleft()
                for dx,dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0<=nx<=m-1 and 0<=ny<=n-1 and heights[nx][ny] >= heights[x][y] and (nx,ny) not in seen:
                        seen.add((nx,ny))
                        q.append((nx,ny))

        pac = set()
        atl = set()        
        for r in range(m):
            bfs(r,0,pac)
        for c in range(n):
            bfs(0,c,pac)
        for r in range(m):
            bfs(r,n-1,atl)
        for c in range(n):
            bfs(m-1,c,atl)
        
        return [[r,c] for r,c in pac & atl]
"""