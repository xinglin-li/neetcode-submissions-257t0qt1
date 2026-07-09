class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 核心：找最短，所以一旦满足 window_sum >= target，就疯狂缩左边。
        # 注意：这题能滑窗，是因为 nums 里都是正数。
        left = 0
        window_sum = 0
        ans = float("inf")

        for right, x in enumerate(nums):
            window_sum += x
            while window_sum >= target:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1
        
        return ans if ans != float("inf") else 0