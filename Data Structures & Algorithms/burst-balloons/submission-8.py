class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        vals = [1] + nums + [1]
        n = len(vals)
        dp = [[0]*n for _ in range(n)]

        # length 为区间长度 j - i
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                # 枚举最后一个戳爆的气球 k
                for k in range(i+1,j):
                    dp[i][j] = max(
                        dp[i][j],
                        vals[i]*vals[k]*vals[j] + dp[i][k] + dp[k][j]
                    )
        return dp[0][n-1]