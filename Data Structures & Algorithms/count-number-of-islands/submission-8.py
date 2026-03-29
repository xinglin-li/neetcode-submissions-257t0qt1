class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r,c):
            if (r<0 or r>m-1 or c<0 or c>n-1 or grid[r][c] == "0" or grid[r][c] == "#"):
                return 
            
            grid[r][c] = "#"

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        is_land = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] =="1":
                    dfs(i,j)
                    is_land +=1
        return is_land

"""
# DFS solution using visited set
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if (
                r < 0 or c < 0 or 
                r >= rows or c >= cols or 
                grid[r][c] == '0' or 
                (r, c) in visited
            ):
                return
            visited.add((r, c))
            # Explore 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        
        return islands

# BFS solution

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            q = deque([(r, c)])
            while q:
                x, y = q.popleft()
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < rows and 0 <= ny < cols and
                        grid[nx][ny] == '1' and
                        (nx, ny) not in visited
                    ):
                        visited.add((nx, ny))
                        q.append((nx, ny))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    visited.add((r, c))
                    bfs(r, c)
                    islands += 1
        
        return islands
"""



