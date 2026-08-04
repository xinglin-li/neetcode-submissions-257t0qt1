class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        x = 1
        for i in range(m+n-2, m-1, -1):
            x *= i
        
        y = 1
        for j in range(1, n):
            y *= j
        
        return x // y
