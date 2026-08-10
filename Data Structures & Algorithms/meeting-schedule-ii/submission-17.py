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
        
        intervals.sort(key=lambda x: x.start)
        # min-heap, stores the minimum END for existing meetings
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0].end)

        for meeting in intervals[1:]:
            # 如果当前会议开始时间 >= 堆顶会议结束时间. 可以复用房间
            if meeting.start >= free_rooms[0]:
                heapq.heappop(free_rooms)
            
            # 不能复用, 则直接入min-heap
            heapq.heappush(free_rooms, meeting.end)
        
        return len(free_rooms)