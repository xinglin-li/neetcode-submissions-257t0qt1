class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda row: row[0])
        i = 1
        res = []
        n = len(intervals)
        s,e = intervals[0]
        for i in range(1,n):
            if intervals[i][0] > e:
                res.append([s,e])
                s,e = intervals[i]
            else:
                e = max(e,intervals[i][1])
        res.append([s,e])
        return res