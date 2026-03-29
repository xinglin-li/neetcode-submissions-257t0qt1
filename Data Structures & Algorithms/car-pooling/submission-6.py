class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []  # (position, passengerChange)

        for p, f, t in trips:
            events.append((f, p))    # pick up
            events.append((t, -p))   # drop off
        
        # 按位置升序排序
        # 如果同一位置，先 drop 再 pick (保证不多算)
        events.sort()

        used = 0
        for _, change in events:
            used += change
            if used > capacity:
                return False
        
        return True