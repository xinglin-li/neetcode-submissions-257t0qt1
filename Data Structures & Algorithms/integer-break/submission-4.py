class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] := max product of interger i breaks into k pos int
        # dp[i] = max(j*(i-j), dp[i-j]*j) for 1<= j < i
        dp = [0]*(n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i],j*(i-j), dp[i-j]*j)
        return dp[n]