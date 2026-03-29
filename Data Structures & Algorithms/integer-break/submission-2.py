class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] = max_{j <= i} dp[i-j]*j
        dp = [i-1 for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(i):
                dp[i] = max(max(j,dp[j])*max(i-j,dp[i-j]),dp[i])
        return dp[n]