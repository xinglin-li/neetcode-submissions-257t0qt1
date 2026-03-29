class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # ceil = (pile + k - 1) // k
        l,r = 1, max(piles)
        def can_finish(k):
            t = 0
            for pile in piles:
                t += (pile + k -1) //k
            return t <= h
        k = r
        while l <= r:
            mid = (l+r)//2
            if can_finish(mid):
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k