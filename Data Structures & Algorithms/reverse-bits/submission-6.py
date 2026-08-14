class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # 32 位固定长度处理
        for _ in range(32):
            # res 左移一位腾出空间，并将 n 的最低位 (n & 1) 放到 res 的最低位
            res = (res << 1) | (n & 1)
            # n 右移一位，准备读取下一个比特位
            n >>= 1
            
        return res