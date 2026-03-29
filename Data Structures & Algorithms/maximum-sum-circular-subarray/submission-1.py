class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # max(max_Kadane, total_sum - min_Kadane)
        total = sum(nums)

        cur_max = max_sum = nums[0]
        cur_min = min_sum = nums[0]

        for x in nums[1:]:
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)

            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)

        # 如果全是负数，不能用环形
        if max_sum < 0:
            return max_sum

        return max(max_sum, total - min_sum)