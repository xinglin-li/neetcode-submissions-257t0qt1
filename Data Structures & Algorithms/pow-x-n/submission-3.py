class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 处理负数指数
        if n < 0:
            x = 1 / x
            n = -n

        res = 1.0
        current_product = x

        # 快速幂: 将指数 n 拆解为二进制
        while n > 0:
            # 若当前最低二进制位为 1, 将当前底数累乘到结果中
            if n & 1:
                res *= current_product
            # 底数平方 + 指数右移 (即除以2)
            current_product *= current_product
            n >>= 1
        return res
