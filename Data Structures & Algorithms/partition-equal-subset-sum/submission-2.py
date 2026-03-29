class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 0/1 Knapsack. 
        # First need to convert it into dp. If the total sum can be divided by 2,
        # then we'll have two subsequences which have equal sum.
        # The problem reduced to 0/1 Knapsack.
        # As long as we can find a sequence sum up to target, then we should return True.
        s = sum(nums)
        if s%2: return False
        target = s//2
        dp = [False]*(target+1)
        dp[0] = True
        for num in nums:
            for t in range(target, num-1,-1):
                dp[t] = dp[t] or dp[t-num]
        return dp[target]
