class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # all integers are positive, and subarray is contiguous
        left = 0
        res = float('inf')
        cumsum = 0
        for i in range(len(nums)):
            cumsum += nums[i]
            while cumsum >= target:
                res = min(res, i-left+1)
                cumsum -= nums[left]
                left += 1
        return res if res != float('inf') else 0
                