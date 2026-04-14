class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp[i] := start from i-th round, max(current player's score - other player's score)
        # dp[i] = max(s - dp[i + k]), s = sum(stoneValue[i:i+k]), s.t. k in {1,2,3}
        n = len(stoneValue)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            dp[i] = float("-inf") # dp[i] 可以为负数
            cum_sum = 0 
            for k in range(3):
                if i + k < n:
                    cum_sum += stoneValue[i+k]
                    dp[i] = max(dp[i], cum_sum - dp[i+k+1])
        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"
        return "Tie"