class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sweep line
        events = []
        for p, s, e in trips:
            events.append((s, p))
            events.append((e, -p))
        events.sort()
        cur = 0
        for _, p in events:
            cur += p
            if cur > capacity:
                return False
        return True