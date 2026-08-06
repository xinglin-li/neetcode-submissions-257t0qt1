class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        from functools import lru_cache
        n = len(piles)
        
        # 1. 计算后缀和 suffix_sum[i] 表示 piles[i:] 的石子总数
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # 2. 记忆化搜索：dp(i, M) 表示从下标 i 开始，在参数 M 下当前玩家能拿到的最大石子数
        @lru_cache(None)
        def dp(i: int, M: int) -> int:
            # 终止条件：若剩余堆数 <= 2M，直接把剩下的全部拿走
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            # 枚举拿取的堆数 X，使得对手在下一步拿到的尽量少，从而让自己拿到的最大
            max_stones = 0
            for X in range(1, 2 * M + 1):
                # 拿走 X 堆后，对手的最大收益是 dp(i + X, max(M, X))
                # 自己能拿到的就是剩余总数 - 对手的最大收益
                max_stones = max(max_stones, suffix_sum[i] - dp(i + X, max(M, X)))
                
            return max_stones

        # 初始从下标 0 开始，M = 1，Alice 率先行动
        return dp(0, 1)

