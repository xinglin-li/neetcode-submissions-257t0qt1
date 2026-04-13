class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]:= 以nums[i]为结尾, 可以得到的LIS length
        # dp[i] = max(dp[i], dp[j]+1) for all j < i, s.t nums[j] < nums[i]
        n = len(nums)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)