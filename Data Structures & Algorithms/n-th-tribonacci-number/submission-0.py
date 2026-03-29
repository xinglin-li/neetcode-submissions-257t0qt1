class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        t_0, t_1, t_2 = 0, 1, 1
        t_3 = 0
        for i in range(2, n):
            t_3 = t_0 + t_1 + t_2
            t_0, t_1, t_2 = t_1, t_2, t_3
        return t_3