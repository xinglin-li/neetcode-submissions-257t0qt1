class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 0/1 Knapsack
        if sum(nums)%2: return False

        target = sum(nums)//2
        dp = [False]*(target+1)
        dp[0] = True

        for num in nums:
            for t in range(target, num - 1, -1):
                dp[t] = dp[t] or dp[t-num]
        
        return dp[target]
