class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = fewest amount needs to represent i
        # dp[i] = min_{j in coins} dp[i-j] + 1
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != float("inf"):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1 
