class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # greedy + binary search on the answer
        # left = max(nums)  (至少要容得下单个最大值)
        # right = sum(nums) (全放一组)
        left, right = max(nums), sum(nums)

        # 检查能否在最大和 <= mid 的情况下分成 <= k 组
        def can_split(max_allowed):
            group_count = 1
            current_sum = 0

            for x in nums:
                if current_sum + x <= max_allowed:
                    current_sum += x
                else:
                    group_count += 1
                    current_sum = x
                    if group_count > k:
                        return False
            return True

        # 二分答案
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left
