class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # dp[j] 表示区间 [i..j] 内先手相对于后手的净胜石子数
        dp = piles[:]
        
        # 从区间长度 2 开始逐步扩展
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # 先手选 piles[i] 或 piles[j]，减去对手在剩余区间的最优净胜收益
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
                
        return dp[-1] > 0