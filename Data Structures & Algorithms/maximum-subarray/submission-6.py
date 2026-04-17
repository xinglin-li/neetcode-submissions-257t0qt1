class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algo. 如果之前的和是负的 → 扔掉, 如果是正的 → 接上.
        cur_max = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            ans = max(ans, cur_max)
        
        return ans