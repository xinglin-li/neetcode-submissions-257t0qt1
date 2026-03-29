class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
            stack = []
            max_area = 0
            heights.append(0)  # 加一个 0，使得所有柱子都能被处理

            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)

                stack.append(i)

            return max_area