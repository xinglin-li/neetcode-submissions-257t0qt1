class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        
        # 基础情况：只有 1 堆石子时，先手直接拿走
        for i in range(n):
            dp[i][i] = piles[i]
            
        # 按照区间长度从小到大计算
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(
                    piles[i] - dp[i + 1][j],  # 选择开头的石子
                    piles[j] - dp[i][j - 1]   # 选择末尾的石子
                )
                
        # dp[0][n-1] 表示整排石子中 Alice 比 Bob 多拿的分数，> 0 代表 Alice 获胜
        return dp[0][n - 1] > 0