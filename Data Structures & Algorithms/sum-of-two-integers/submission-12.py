class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF      # limit to 32 bits
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK  # sum & carry

        # handle negative numbers (two’s complement)
        # return a if a <= MAX_INT else -(a ^ MASK) - 1
        return a if a <= MAX_INT else ~(a ^ MASK)