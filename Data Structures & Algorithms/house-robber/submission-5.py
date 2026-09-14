class Solution:
    def rob(self, nums: List[int]) -> int:
        lag1 = lag2 = 0
        for x in nums:
            curr = max(lag1, lag2 + x)
            lag2 = lag1
            lag1 = curr
        return curr
