class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[i][j] := min sum to (i,j)
        # dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        m, n = len(grid), len(grid[0])
        
        dp = [float('inf')] * (n + 1)
        dp[1] = 0   # 核心 trick
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[j] = min(dp[j], dp[j-1]) + grid[i-1][j-1]
        
        return dp[n]
