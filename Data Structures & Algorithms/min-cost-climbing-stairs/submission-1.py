class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp[i] 只依赖 dp[i-1], dp[i-2]
        dp1, dp2 = 0, 0     # dp[-1], dp[0]

        for i in range(2, n+1):
            dpi = min(dp1 + cost[i-1], dp2 + cost[i-2])
            dp1, dp2 = dpi, dp1

        return dp1