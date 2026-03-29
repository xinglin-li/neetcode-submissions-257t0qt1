class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left + right)//2
            sq = mid*mid
            if sq == x:
                return mid
            elif sq > x:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1