class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(money):
            n = len(money)
            if n == 0:
                return 0
            if n == 1:
                return money[0]
            if n == 2:
                return max(money[0], money[1])
            
            dp = [0]*n
            dp[0], dp[1] = money[0], max(money[0], money[1])
            for i in range(2, n):
                dp[i] = max(money[i] + dp[i-2], dp[i-1])
            return dp[n-1]
        
        if len(nums) == 1:
            return nums[0]
        
        return max(helper(nums[:-1]), helper(nums[1:]))