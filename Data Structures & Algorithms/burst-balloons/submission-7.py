class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp[i,j]: 戳爆开区间 $(i, j)$ 内所有气球所能获得的最大硬币数
        from functools import cache
        # 1. 首尾补 1，消除边界讨论
        vals = [1] + nums + [1]

        # 2. 记忆化搜索：开区间 (i, j)
        @cache
        def dp(i,j):
            if i+1>=j:
                return 0
            max_coins = 0
            # 枚举区间 (i, j) 内最后一个被戳爆的气球 k
            for k in range(i+1, j):
                coins = vals[i]*vals[k]*vals[j] + dp(i,k) + dp(k,j)
                max_coins = max(max_coins, coins)
            return max_coins
        return dp(0, len(vals)-1)