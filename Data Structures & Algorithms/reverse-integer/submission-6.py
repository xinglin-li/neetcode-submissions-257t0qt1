class Solution:
    def reverse(self, x: int) -> int:
        # 定义 32 位有符号整数的边界
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        res = 0
        # 统一按正数处理，最后再还原符号，这样可以避开 Python 负数除法/取模的坑
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            # 1. 弹出最后一位
            digit = x % 10
            x //= 10
            
            # 2. 核心：提前检查溢出
            # 我们即将执行 res = res * 10 + digit
            # 所以要判断 res 是否会超过 INT_MAX // 10
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0
            
            # 3. 推入最后一位
            res = res * 10 + digit
            
        return res * sign