class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_xor = 0
        for x in nums:
            total_xor |= x
        return total_xor * (1 << (len(nums) - 1))