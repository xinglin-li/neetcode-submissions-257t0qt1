class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, x in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < x:
                prev_i = stack.pop()
                ans[prev_i] = i - prev_i
            stack.append(i)
        return ans

