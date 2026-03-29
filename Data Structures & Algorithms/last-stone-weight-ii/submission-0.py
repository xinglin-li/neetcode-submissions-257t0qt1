class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 0/1 背包（subset sum）问题
        S = sum(stones)
        target = S // 2
        dp = [False]*(target+1)
        dp[0] = True
        for w in stones:
            for j in range(target, w-1,-1):
                dp[j] |= dp[j-w]
        for j in range(target,-1,-1):
            if dp[j]:
                return S - 2*j