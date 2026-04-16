class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i][j] := advantage of player start at piles[i:j] (closed set)
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        
        for length in range(2, n+1):
            # i + len - 1 < n
            # i < n - len + 1
            for i in range(n-length+1):
                # j - i  + 1 = length, since this is inclusive interval
                j = length + i - 1 
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        return dp[0][n-1] > 0