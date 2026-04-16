class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # P + N = target; P - N = sum(nums) -> P = (target + sum(nums))/2
        # 0/1 knapsack 
        s = sum(nums)
        if s < target or (target+s)%2 != 0:
            return 0
        P = (target+s)//2
        dp = [0]*(P+1)
        dp[0] = 1
        for num in nums:
            for i in range(P, num-1, -1):
                dp[i] += dp[i-num]
        return dp[P]