class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        INF = amount + 1  # a large enough number
        dp = [INF] * (amount + 1)
        dp[0] = 0
        
        for x in range(1, amount + 1):
            for c in coins:
                if x - c >= 0:
                    dp[x] = min(dp[x], dp[x - c] + 1)
        
        return dp[amount] if dp[amount] != INF else -1


"""
from functools import lru_cache

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(rem):
            if rem == 0: return 0
            if rem < 0: return float('inf')
            return min(dfs(rem - c) + 1 for c in coins)
        
        ans = dfs(amount)
        return ans if ans != float('inf') else -1

"""