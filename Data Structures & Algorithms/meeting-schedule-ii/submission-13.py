"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # use minHeap to simulate the process
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        minHeap = [0]
        for interval in intervals:
            start = interval.start
            end = interval.end
            if start >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
        return len(minHeap)
