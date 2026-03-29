class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        l, r = 0, n-1
        while l< r:
            w = r - l
            s = min(heights[l],heights[r])*w
            res = max(res,s)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res