class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed

                if hours > h:
                    return False
            return True
        
        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            if can_finish(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
