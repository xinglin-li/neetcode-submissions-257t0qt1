class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # target = sum(nums)//2
        # dp[i] := i can is the sum of subset of nums
        # dp[i] = dp[i] or dp[i-num] for num in nums
        # 0/1 knapsack, backward traverse
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target]



