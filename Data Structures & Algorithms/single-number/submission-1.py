class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR满足交换律, 结合律.
        # a^0 = a, a^a = 0
        # a^b^a^b^c = a^a^b^b^c = (a^a)^(b^b)^c = 0^0^c = c
        xor = 0
        for num in nums:
            xor^=num
        return xor