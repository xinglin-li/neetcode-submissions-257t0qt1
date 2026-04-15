class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[i][j] := # of possible paths to (i,j)
        # dp[i][j] = 0 if obstacleGrid[i][j] == 1
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])    
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if (i,j) == (1,1):
                    continue
                if obstacleGrid[i-1][j-1] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m][n]