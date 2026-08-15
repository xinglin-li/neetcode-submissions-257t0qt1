class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = (1<<32) - 1
        MAX_INT = (1<<31) - 1
        while b:
            carry = (a&b) << 1
            a = (a^b) & MASK
            b = carry & MASK
        # ~(a) = - (a + 1), e.g. ~0 = -1
        # a^MASK -> 超过32全部为0, 32位以内翻转. ~(a^MASK)超过32全部为1, 32位以内翻转回原来的样子. 正好符合python对负数的定义
        return a if a <= MAX_INT else ~(a^MASK) 