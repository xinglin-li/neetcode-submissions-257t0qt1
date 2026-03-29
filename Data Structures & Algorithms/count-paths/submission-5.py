class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1d optimized
        # dp[j] (dp[i][j]) = dp[j] (dp[i-1][j]) + dp[j-1] (dp[i][j-1])
        dp = [1]*n
        for _ in range(1,m):
            for j in range(1,n):
                dp[j] += dp[j-1]
        return dp[-1]

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n]*m
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
"""

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # C(m-1 + n-1, m-1)
        return math.comb(m-1+n-1,m-1)
"""