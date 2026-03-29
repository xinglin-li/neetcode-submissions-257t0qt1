class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR。相同为0，不同为1
        # XOR 满足交换律(Commutative law) & 结合律 (Associative law)
        xor = 0
        for num in nums:
            xor ^= num
        return xor
