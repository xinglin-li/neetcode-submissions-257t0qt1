class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        dq = deque()  # store indices
        res = []

        for r in range(len(nums)):
            # 1. remove smaller items from the back
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()
            dq.append(r)

            # 2. remove leftmost if it's out of window
            if dq[0] <= r - k:
                dq.popleft()

            # 3. window size reaches k -> record result
            if r >= k - 1:
                res.append(nums[dq[0]])

        return res