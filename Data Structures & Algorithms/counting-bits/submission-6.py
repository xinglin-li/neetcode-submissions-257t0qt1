class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp[i] = dp[i>>1] + (i&1)
        # e.g. 1101的1的数量 = 110的1的数量+最后一位, 最后一位就是i&1
        dp = [0]*(n+1)
        for i in range(1, n+1):
            dp[i] = dp[i>>1] + (i&1)
        return dp
