class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 贪心核心：按区间的右端点（结束时间）升序排序
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1] # 记录上一个被保留区间的结束时间

        for i in range(1, len(intervals)):
            # 当前区间起点 < 上一个去区间END -> OVERLAP
            if intervals[i][0] < prev_end:
                count += 1 # greedy: drop current interval since END_i > prev_end
            else:
                # non-overlapping: keep current interval, and update 'prev_end'.
                prev_end = intervals[i][1]
        
        return count
