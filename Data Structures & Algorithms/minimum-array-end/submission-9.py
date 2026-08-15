class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # Bit insertion, 位填充
        # 1. num & x == x, x为1的位置, 所有num在该位置也必须为1
        # 2. 将数字插入非1的位置.
        
        k = n - 1
        res = x
        bit_pos = 0
        
        # 将 k 的二进制位依次填补到 x 的 0 对应位置上
        while k > 0:
            # 如果当前位置在 x 中为 0，则将 k 的最低位填入该位置
            if (res & (1 << bit_pos)) == 0:
                res |= (k & 1) << bit_pos
                k >>= 1  # k 右移，准备填入下一位
                
            bit_pos += 1  # 检查 res 的下一个二进制位
            
        return res