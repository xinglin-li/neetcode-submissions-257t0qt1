class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total_sum = sum(stones)
        target = total_sum // 2
        
        # 初始化 (n+1) x (target+1) 的二维矩阵
        # dp[i][j] 表示前 i 个石头在容量为 j 时的最大重量
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            curr_weight = stones[i-1]
            for j in range(target + 1):
                if j < curr_weight:
                    # 容量不够，只能继承不选该石头的结果
                    dp[i][j] = dp[i-1][j]
                else:
                    # 在“不选”和“选”之间取最大值
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - curr_weight] + curr_weight)
        
        # 结果依然是总重减去两倍的最大子集重量
        return total_sum - 2 * dp[n][target]