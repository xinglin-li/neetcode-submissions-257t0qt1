class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(i,j):
            if dp[i][j] != 0:
                return dp[i][j]
            
            best = 1

            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    best = max(best, 1 + dfs(x,y))
            
            return best
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j))
        
        return res

