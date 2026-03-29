class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = nums[0]
        n = len(nums)
        for i in range(1,n):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(cur_sum,max_sum)
        return max_sum

