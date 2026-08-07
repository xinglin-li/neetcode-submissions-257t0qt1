class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 1. 正常的Kadane; 2. 跨首尾 total_sum - min_Kadane
        # max(max_Kadane, total_sum - min_Kadane)
        total = 0
        max_sum = nums[0]
        cur_max = 0
        min_sum = nums[0]
        cur_min = 0

        for x in nums:
            # 维护最大子数组和 (Kadane)
            cur_max = max(cur_max + x, x)
            max_sum = max(max_sum, cur_max)
            # 维护最小子数组和
            cur_min = min(cur_min + x, x)
            min_sum = min(min_sum, cur_min)

            total += x
        
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total - min_sum)