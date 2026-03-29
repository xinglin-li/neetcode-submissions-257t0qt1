class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(rate):
            cost = 0
            for p in piles:
                cost += math.ceil(p/rate)
                if cost > h:
                    return False
            return True

        l, r = 1, max(piles)

        while l < r:
            mid = (l+r)//2
            if can_eat(mid):
                r = mid
            else:
                l = mid + 1
        return l