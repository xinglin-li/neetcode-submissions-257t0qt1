class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[1])
        remove = 0
        prev_e = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < prev_e:
                remove += 1
            else:
                prev_e = intervals[i][1]
        return remove
        