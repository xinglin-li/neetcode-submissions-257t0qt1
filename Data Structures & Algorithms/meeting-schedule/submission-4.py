"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 按会议开始时间排序
        intervals.sort(key=lambda x: x.start)
        
        # 依次检查前后相邻的两个会议是否冲突
        for i in range(1, len(intervals)):
            # 下一个会议的开始时间 < 上一个会议的结束时间 -> 时间冲突
            if intervals[i].start < intervals[i - 1].end:
                return False
                
        return True
