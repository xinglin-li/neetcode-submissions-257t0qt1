class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = nums[0]
        cur_max = nums[0]
        res = cur_max
        for i in range(1, len(nums)):
            x = nums[i]
            candidates = (x, x*cur_min, x*cur_max)
            cur_min = min(candidates)
            cur_max = max(candidates)
            res = max(res, cur_max)
        return res