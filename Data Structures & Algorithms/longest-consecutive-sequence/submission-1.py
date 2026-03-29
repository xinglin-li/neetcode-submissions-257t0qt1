class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for x in s:
            if x - 1 not in s:           # start of a sequence
                y = x
                length = 1
                while y + 1 in s:
                    y += 1
                    length += 1
                best = max(best, length)

        return best
        