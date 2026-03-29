class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # max(max_Kadane, total_sum - min_Kadane)
        total_sum = sum(nums)
        cur_max = max_sum = nums[0]
        cur_min = min_sum = nums[0]

        for num in nums[1:]:
            cur_max = max(cur_max + num, num)
            max_sum = max(cur_max, max_sum)
            cur_min = min(cur_min + num, num)
            min_sum = min(cur_min, min_sum)
        
        if max_sum < 0:
            return max_sum

        return max(max_sum,total_sum - min_sum)