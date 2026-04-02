class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # game theory. dp[i]: 从i开始能多出的最大分数
        n = len(stoneValue)
        dp = [float("-inf")]*n + [0]
        for i in range(n-1,-1,-1):
            cum_sum = 0
            for j in range(3):
                if i + j < n:
                    cum_sum += stoneValue[i+j]
                    dp[i] = max(dp[i], cum_sum - dp[i+j+1])
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
