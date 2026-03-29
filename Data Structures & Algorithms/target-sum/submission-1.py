class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # This question requires insights
        # P - N = target, where P is the sum of positive part and N is the sum of negative part
        # P + N = sum(nums)
        # 2P = target + sum(nums) -> P = (target + sum(nums))/2
        # 0/1 Knapsack problem

        s = sum(nums)
        if s < abs(target) or (target + s)%2: return 0
        p = (target + s)//2

        dp = [0]*(p+1)
        dp[0] = 1
        for num in nums:
            for i in range(p,num-1,-1):
                dp[i] += dp[i-num]
        return dp[p]
