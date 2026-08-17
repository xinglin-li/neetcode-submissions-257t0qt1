from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        from functools import cache
        n = len(piles)
        # 计算后缀和，suffix_sum[i] 表示从 piles[i] 到末尾的总石子数
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @cache
        def dfs(i: int, m: int) -> int:
            # 剩余石子可全部取完
            if i + 2 * m >= n:
                return suffix_sum[i]
                
            # 枚举当前回合拿 X 堆 (1 <= X <= 2M)，使对手拿到的石子最少
            min_opponent = float('inf')
            for x in range(1, 2 * m + 1):
                min_opponent = min(min_opponent, dfs(i + x, max(m, x)))
                
            return suffix_sum[i] - min_opponent
            
        return dfs(0, 1)