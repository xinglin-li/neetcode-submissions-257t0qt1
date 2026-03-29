class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, x in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < x:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
