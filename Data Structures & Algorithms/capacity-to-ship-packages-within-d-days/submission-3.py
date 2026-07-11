class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        def can_ship(cap):
            cum_weights = 0
            count_days = 1
            for weight in weights:
                if cum_weights + weight <= cap:
                    cum_weights += weight
                else:
                    cum_weights = weight
                    count_days += 1
                if count_days > days:
                    return False
            return True
        
        while l <= r:
            mid = l + (r - l) // 2
            if can_ship(mid):
                r =  mid - 1
            else:
                l = mid + 1
        
        return l