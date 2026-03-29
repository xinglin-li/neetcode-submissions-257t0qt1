class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        f = [1,2]
        for i in range(2,n):
            f[0], f[1] = f[1], f[0] + f[1]
        return f[1]
"""