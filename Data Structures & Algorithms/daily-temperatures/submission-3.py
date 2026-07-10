class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * (len(temperatures))
        stack = []

        for current_day, current_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < current_temp:
                ans[stack[-1]] = current_day - stack[-1]
                stack.pop()
            stack.append(current_day)
        
        return ans