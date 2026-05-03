class Solution:
    def minEnd(self, n: int, x: int) -> int:
        count = n -1
        res = x
        i = 0
        j = 0
        while (count >> i) > 0:
            if (res >> j) & 1 == 0:
                res |= ((count >> i) & 1) << j
                i += 1
            j += 1
        return res
