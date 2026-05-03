class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = -1 if x < 0 else 1
        res = 0
        
        while x != 0:
            digit = sign*(abs(x) % 10)
            x = int(x / 10)
            
            # 🚨 关键：提前判断是否溢出
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0
            if res < int(INT_MIN / 10) or (res == int(INT_MIN / 10) and digit < -8):
                return 0
            
            res = res * 10 + digit
        
        return res