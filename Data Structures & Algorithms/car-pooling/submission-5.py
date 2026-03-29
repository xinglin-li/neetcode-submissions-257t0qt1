class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for cap, start, end in trips:
            events.append((start,cap))
            events.append((end,-cap))
        
        events.sort()
        used = 0
        for _, change in events:
            used += change
            if used > capacity:
                return False
        return True