class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # 上
                    if i == 0 or grid[i-1][j] == 0:
                        perimeter += 1
                    # 下
                    if i == m-1 or grid[i+1][j] == 0:
                        perimeter += 1
                    # 左
                    if j == 0 or grid[i][j-1] == 0:
                        perimeter += 1
                    # 右
                    if j == n-1 or grid[i][j+1] == 0:
                        perimeter += 1
        
        return perimeter