class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 0/1 knapsack + combination
        dp = [0]*(amount+1)
        dp[0] = 1 # 0 = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]