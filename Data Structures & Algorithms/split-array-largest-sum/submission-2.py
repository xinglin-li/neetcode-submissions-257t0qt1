class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # greedy + binary search on the answer
        # left = max(nums)  (至少要容得下单个最大值)
        # right = sum(nums) (全放一组)
        left, right = max(nums), sum(nums)

        # 检查能否在最大和 <= mid 的情况下分成 <= k 组
        def can_ship(cap):
            count_group = 1
            cum_sum = 0
            for num in nums:
                if cum_sum + num <= cap:
                    cum_sum += num
                else:
                    count_group += 1
                    if count_group > k:
                        return False
                    cum_sum = num
            return True

        # 二分答案
        while left < right:
            mid = (left+right)//2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left