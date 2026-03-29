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
        intervals.sort(key=lambda x: x.end)
        intervals.sort(key=lambda x: x.start)
        def find_overlap(intervals):
            removed = []
            e = intervals[0].end
            for i in range(1,len(intervals)):
                if intervals[i].start < e:
                    removed.append(intervals[i])
                else:
                    e = intervals[i].end
            return removed

        day = 1
        removed = find_overlap(intervals)
        while removed:
            removed = find_overlap(removed)
            day += 1
        return day

"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])

        heap = []  # end times
        for s, e in intervals:
            if heap and heap[0] <= s:   # room becomes free
                heapq.heappop(heap)
            heapq.heappush(heap, e)
        return len(heap)

"""
                