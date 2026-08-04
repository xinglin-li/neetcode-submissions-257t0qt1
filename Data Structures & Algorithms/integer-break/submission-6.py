class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] := the maximum product get can get for i, which split i into at least two elements
        # dp[i] = max_{1<=j<i}(max(j*(i-j), j*dp[i-j]))
        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]