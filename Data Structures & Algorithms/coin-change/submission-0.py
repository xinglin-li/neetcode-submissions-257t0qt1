class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [INF]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        if dp[amount] == INF:
            return -1
        return dp[amount]


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