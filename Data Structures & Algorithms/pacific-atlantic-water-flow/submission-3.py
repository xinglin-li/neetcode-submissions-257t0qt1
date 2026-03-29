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