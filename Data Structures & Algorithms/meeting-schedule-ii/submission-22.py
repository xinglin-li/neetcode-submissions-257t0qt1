"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        # 模拟, 不仅要知道会议入堆的顺序. 还要知道入堆时, 之前的会议结束与否
        intervals.sort(key=lambda x: x.start)
        # min-heap, stores the minimum END for existing meetings
        rooms = [intervals[0].end]
        for interval in intervals[1:]:
            start = interval.start
            if rooms[0] <= start:
                heapq.heappop(rooms) 
            heapq.heappush(rooms, interval.end)
        return len(rooms)

