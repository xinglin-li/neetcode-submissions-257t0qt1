class Solution:
    def hammingWeight(self, n: int) -> int:
        # n - 1时候, 最右边的1变成0, 他后面的0全变成1, 其他位置不变. 所以n&(n-1)会把最右边的 1 变成 0. 
        count = 0
        while n:
            n = n&(n-1)
            count += 1
        return count