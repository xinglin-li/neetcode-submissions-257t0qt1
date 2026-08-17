class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algo. 如果之前的和是负的 → 扔掉, 如果是正的 → 接上.
        ans = curr_max = nums[0]

        for num in nums[1:]:
            curr_max = max(num, curr_max + num)
            ans = max(curr_max, ans)
        
        return ans