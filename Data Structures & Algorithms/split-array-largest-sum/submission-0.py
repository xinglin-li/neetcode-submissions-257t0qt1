class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # greedy + binary search on the answer
        left, right = max(nums), sum(nums)

        def can_divide(capacity):
            cumsum = 0
            segments = 1
            for num in nums:
                if cumsum + num <= capacity:
                    cumsum += num
                else:
                    cumsum = num
                    segments += 1
            return segments <= k
        
        while left < right:
            mid = (left + right)//2
            if can_divide(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
