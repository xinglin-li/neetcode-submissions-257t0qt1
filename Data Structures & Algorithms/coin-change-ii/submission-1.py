class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 完全背包（unbounded knapsack）+ 组合数（order does NOT matter）
        dp = [0]*(amount + 1)
        dp[0] = 1 # only empty set is satisfied

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        
        return dp[amount]