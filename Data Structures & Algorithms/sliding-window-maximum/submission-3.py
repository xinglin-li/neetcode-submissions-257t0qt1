class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque()  # store indices, nums[dq] is decreasing
        res = []

        for r, x in enumerate(nums):
            # 1) maintain decreasing deque
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(r)

            # 2) remove out-of-window index from front
            left = r - k + 1
            if dq[0] < left:
                dq.popleft()

            # 3) record answer when window is formed
            if r >= k - 1:
                res.append(nums[dq[0]])

        return res