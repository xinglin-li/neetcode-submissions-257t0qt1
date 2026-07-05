class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:
                cur = x
                length = 1
                while cur + 1 in s:
                    cur += 1
                    length += 1
                
                best = max(best, length)
        return best

