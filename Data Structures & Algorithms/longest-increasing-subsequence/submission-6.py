class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        tails = []
        for num in nums:
            l,r = 0, len(tails)
            while l<r:
                m = (l+r)//2
                if tails[m] < num:
                    l = m+1
                else:
                    r = m
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num
        return len(tails)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1]*n

        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
"""