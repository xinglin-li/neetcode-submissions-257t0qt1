class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # right, up, left, down
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        perimeter = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in dirs:
                        x = i + dx
                        y = j + dy
                        if x < 0 or x > m-1 or y < 0 or y > n-1 or grid[x][y] == 0:
                            perimeter += 1
        return perimeter