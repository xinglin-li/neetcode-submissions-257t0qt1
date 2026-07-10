class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 核心：单调递减队列，队头永远是当前窗口最大值。
        q = deque()
        ans = []
        for right, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(right)
            left = right - k + 1

            if q[0] < left:
                q.popleft()
            
            if right >= k - 1:
                ans.append(nums[q[0]])
        
        return ans
