class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # (S - neg) - neg. neg <= S//2
        # 0/1 kanpsack to find group of stones closest to S//2
        target = sum(stones)//2
        dp = [0]*(target+1)
        for stone in stones:
            for j in range(target, stone-1, -1):
                dp[j] = max(dp[j], dp[j-stone] + stone)
        return sum(stones) - 2*dp[target]