class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            w = r-l
            s = w*min(heights[l], heights[r])
            res = max(res, s)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res