class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = (left+right)//2
            sq_mid = mid*mid
            if sq_mid == x:
                return mid
            elif sq_mid > x:
                right = mid -1
            else:
                left = mid + 1
        return left - 1