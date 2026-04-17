class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for length in range(2, n):
            # length = j - i
            # j = length + i, j < n -> i < n - length
            for i in range(n - length):
                j = length + i
                for k in range(i+1,j):
                    # Important: k is the last balloon burst.
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
        return dp[0][n-1]