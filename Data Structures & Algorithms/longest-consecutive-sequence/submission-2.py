class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for x in s:  # 遍历 set（去重后更干净）
            if x - 1 not in s:          # 只从起点开始
                y = x
                while y in s:
                    y += 1
                best = max(best, y - x)  # y 是第一个不在 s 的数

        return best