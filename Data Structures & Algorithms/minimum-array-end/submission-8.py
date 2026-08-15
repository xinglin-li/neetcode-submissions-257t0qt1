class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Bit insertion, 位填充
        # 1. num & x == x, x为1的位置, 所有num在该位置也必须为1
        # 2. 将数字插入非1的位置.
        
        k = n - 1
        ans = x
        bit = 1

        while k:
            # 只有 x 原本为 0 的位置可以填
            if (x & bit) == 0:
                if k & 1:
                    ans |= bit
                k >>= 1

            bit <<= 1

        return ans