class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # 我们需要填入的数值是 n - 1
        count = n - 1
        res = x
        
        i = 0 # 遍历 res 的每一位
        j = 0 # 遍历 count 的每一位
        
        # 只要 count 还没填完
        while (count >> j) > 0:
            # 如果 res 的第 i 位是 0，说明这是个“空位”
            if (res >> i) & 1 == 0:
                # 把 count 的第 j 位搬到 res 的第 i 位
                if (count >> j) & 1:
                    res |= (1 << i)
                j += 1
            i += 1
            
        return res