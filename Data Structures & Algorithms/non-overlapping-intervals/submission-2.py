class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        keep = 0
        prev_e = float("-inf")
        for s,e in intervals:
            if s >= prev_e:
                keep += 1
                prev_e = e
        return len(intervals) - keep