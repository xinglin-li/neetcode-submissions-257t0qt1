class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algo. 如果之前的和是负的 → 扔掉, 如果是正的 → 接上.
        max_sum = cur_sum = nums[0]
        for x in nums[1:]:
            # 若前缀和小于 0 则舍弃，从 x 重新开始
            cur_sum = max(x, cur_sum + x)
            max_sum = max(max_sum, cur_sum)
        return max_sum