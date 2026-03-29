class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0
        for s in nums_set:
            if s-1 not in nums_set:
                longest = 1
                while s+1 in nums_set:
                    longest += 1
                    s += 1
                best = max(best, longest)
        return best
        