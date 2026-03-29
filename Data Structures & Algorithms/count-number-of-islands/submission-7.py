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



