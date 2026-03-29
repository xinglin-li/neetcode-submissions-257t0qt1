class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Binary search on the answer
        # 搜索区间：船的最小容量 = max(weights)
        #        船的最大容量 = sum(weights)
        left, right = max(weights), sum(weights)
        def can_ship(cap):
            count = 1
            cum_weight = 0
            for weight in weights:
                if cum_weight + weight <= cap:
                    cum_weight += weight
                else:
                    cum_weight = weight
                    count += 1
                if count > days: return False
            return True
        
        while left < right:
            mid = (left + right)//2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1

        return left

