class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # all integers are positive, and subarray is contiguous
        l = 0
        ans = float("inf")
        cumsum = 0
        for r in range(len(nums)):
            cumsum += nums[r]
            while cumsum >= target:
                ans = min(ans, r-l+1)
                cumsum -= nums[l]
                l += 1
        return ans if ans != float("inf") else 0
                