class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # This is called "Interval DP".
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # len = interval length
        for length in range(2, n):       # 至少隔一个气球
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k] + dp[k][right] + nums[left]*nums[k]*nums[right]
                    )

        return dp[0][n-1]