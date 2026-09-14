class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = nums[0] # minimum product subarray ends at i
        cur_max = nums[0] # maximum product subarray ends at i
        res = cur_max
        for x in nums[1:]:
            states = (x, x*cur_min, x*cur_max)
            cur_min = min(states)
            cur_max = max(states)
            res = max(res, cur_max)
        return res
        
