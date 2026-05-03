class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Brian Kernighan 算法
        while left < right:
            right = right & (right - 1)
        return right