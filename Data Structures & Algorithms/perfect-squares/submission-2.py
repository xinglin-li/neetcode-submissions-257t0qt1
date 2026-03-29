class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            sq_i = i*i
            if sq_i < n+1:
                dp[sq_i] = 1
            for j in range(i):
                dp[i] = min(dp[i-j]+dp[j],dp[i])
        return dp[-1]