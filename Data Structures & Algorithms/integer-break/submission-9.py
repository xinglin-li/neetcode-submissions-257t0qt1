class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i]:= i 拆分后的最大乘积
        dp = [0] * (n + 1)
        dp[2] = 1

        for i in range(3, n + 1):
            # 将 i 拆分为 j 和 (i - j)
            # 把 $i$ 拆成两份，拆出数对 $(j, i - j)$ 与 $(i - j, j)$ 在数值上是对称的。
            # 当 $j > \lfloor i / 2 \rfloor$ 时，产生的拆分组合在前半段已经全部计算过，继续遍历属于重复计算。
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], j * (i - j), dp[i - j]*j)
        return dp[n]