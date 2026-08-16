class Solution:
    def climbStairs(self, n: int) -> int:
        # 边界条件：n <= 2 时直接返回 n
        if n <= 2:
            return n
        
        # 状态压缩：dp[i] = dp[i-1] + dp[i-2]
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
            
        return curr