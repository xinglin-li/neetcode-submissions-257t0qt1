class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        
        # 逐位反转
        while x > 0:
            res = res * 10 + x % 10
            x //= 10
            
        res *= sign
        
        # 校验 32 位有符号整数溢出范围 [-2^31, 2^31 - 1]
        if res < -2**31 or res > 2**31 - 1:
            return 0
            
        return res