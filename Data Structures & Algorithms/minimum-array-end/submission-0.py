class Solution:
    def minEnd(self, n: int, x: int) -> int:
        k = n - 1
        digit = 0
        while k:
            if x & (1 << digit) == 0:
                if k & 1:
                    x |= (1 << digit)
                k >>= 1  
            digit += 1
        return x
