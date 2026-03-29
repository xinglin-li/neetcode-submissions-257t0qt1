class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        dp = [nums[0], max(nums[0],nums[1])]

        for i in range(2, len(nums)):
            dp[1], dp[0] = max(dp[1], dp[0] + nums[i]), dp[1]

        return dp[1] 