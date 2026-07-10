class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic increasing stack
        # the key is start = index, start = prev_start. -> find the left most index with height > current height
        # 所以stack里面存了, height, 以及左边的起始位置.
        max_area = 0
        stack = []
        heights.append(0)

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                prev_start, prev_height = stack.pop()
                width = index - prev_start
                max_area = max(max_area, width*prev_height)
                start = prev_start
            stack.append((start, height))
        
        return max_area
