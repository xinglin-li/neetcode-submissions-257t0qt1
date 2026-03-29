class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        s = 0
        while l < r:
            h_l, h_r = heights[l], heights[r]
            if heights[l] < heights[r]:
                s = max(s, (r-l)*h_l)
                l += 1
            else:
                s = max(s, (r-l)*h_r)
                r -= 1
        return s