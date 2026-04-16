from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # dp[i][M] := the gain start from i, pick M.
        n = len(piles)
        suffix = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suffix[i] = piles[i] + suffix[i+1]
        
        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0
            if i + M >= n:
                return suffix[i]
            best = 0
            for x in range(1, 2*M + 1):
                best = max(best, suffix[i] - dp(i+x,max(M,x)))
            return best
        return dp(0,1)                
        