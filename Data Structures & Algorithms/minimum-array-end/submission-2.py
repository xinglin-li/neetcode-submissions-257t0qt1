class Solution:
    def minEnd(self, n: int, x: int) -> int:
        k = n - 1
        ans = x
        bit = 0

        while k > 0:
            if ((x >> bit) & 1) == 0:
                if k & 1:
                    ans |= (1 << bit)
                k >>= 1
            bit += 1

        return ans
