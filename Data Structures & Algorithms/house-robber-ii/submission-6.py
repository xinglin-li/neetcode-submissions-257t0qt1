class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def rob(gain):
            prev1, prev2 = 0, 0
            ans = 0
            for x in gain:
                ans = max(prev2 + x, prev1)
                prev2 = prev1
                prev1 = ans
            return ans
        
        return max(rob(nums[1:]), rob(nums[:-1]))

