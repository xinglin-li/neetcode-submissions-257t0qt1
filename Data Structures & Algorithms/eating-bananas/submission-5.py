class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            time = 0
            for pile in piles:
                time += (pile + speed - 1) // speed
                if time > h:
                    return False
            return True
             
        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2
            if can_finish(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left       