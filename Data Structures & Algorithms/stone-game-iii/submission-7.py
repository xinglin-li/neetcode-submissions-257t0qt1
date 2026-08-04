class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # 相对分差（净胜分）
        # dp[i] := max value for player can get if facing stoneValue[i...], max(current player's score - other player's score)
        # dp[i] = max(s - dp[i + k]), s = sum(stoneValue[i:i+k]), s.t. k in {1,2,3}
        # $$dp[i] = \max_{1 \le k \le 3} \left( \left( \sum_{m=0}^{k-1} \text{stoneValue}[i+m] \right) - dp[i+k] \right)$$
        n = len(stoneValue)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            dp[i] = float("-inf")
            take = 0
            for k in range(1, 4):
                if i + k - 1 < n:
                    take += stoneValue[i + k -1]
                    dp[i] = max(dp[i], take - dp[i+k])
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"