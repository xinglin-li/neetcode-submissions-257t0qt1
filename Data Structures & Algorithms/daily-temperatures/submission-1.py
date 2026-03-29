class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack
        n = len(temperatures)
        res = [0] * n
        stack = []  # 存储的是索引 index

        for i, temp in enumerate(temperatures):
            # 如果当前温度比栈顶温度高，说明找到“下一次变暖”
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev  # 计算天数差
            stack.append(i)
        return res