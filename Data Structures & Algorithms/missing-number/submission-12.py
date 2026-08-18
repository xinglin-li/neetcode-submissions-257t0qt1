class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0 ^ X = X
        # X^X = 0
        res = len(nums)
        for i, num in enumerate(nums):
            res ^= i^num
        return res
