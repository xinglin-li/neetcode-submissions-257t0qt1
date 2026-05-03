class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = (1<<32) - 1
        MAX_INT = (1<<31) - 1
        while b:
            carry = (a&b) << 1
            a = (a^b) & MASK
            b = carry & MASK
        return a if a <= MAX_INT else ~(a^MASK) 