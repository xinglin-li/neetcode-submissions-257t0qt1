class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Binary search on the answer
        # 搜索区间：船的最小容量 = max(weights)
        #        船的最大容量 = sum(weights)
        left, right = max(weights), sum(weights)

        def canShip(cap):
            """给定容量 cap，判断能否在 days 天内运完"""
            need_days = 1
            cur = 0
            for w in weights:
                if cur + w > cap:
                    need_days += 1
                    cur = 0
                cur += w
            return need_days <= days

        # 二分最小可行容量
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid   # 可以 ship，尝试更小容量
            else:
                left = mid + 1

        return left