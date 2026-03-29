class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Binary search on the answer
        left, right = max(weights), sum(weights)
        n = len(weights)
        def canShip(capacity):
            need_days = 1
            cur_load = 0
            i = 0
            while i < n:
                if cur_load + weights[i] <= capacity:
                     cur_load += weights[i]
                     i += 1
                else:
                    cur_load = 0
                    need_days += 1 
            return  need_days <= days
        
        while left < right:
            mid = (left + right)//2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left