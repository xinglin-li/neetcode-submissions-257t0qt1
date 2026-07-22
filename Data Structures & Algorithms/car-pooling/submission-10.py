class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for num, start, end in trips:
            events.append((start, num))   # 上车事件
            events.append((end, -num))   # 下车事件
            
        # 按时间戳升序排序；若时间相同，下车事件（-num）排在前面（先下后上）
        events.sort(key=lambda x: (x[0], x[1]))
        
        curr_passengers = 0
        for time, num_change in events:
            curr_passengers += num_change
            if curr_passengers > capacity:
                return False
                
        return True