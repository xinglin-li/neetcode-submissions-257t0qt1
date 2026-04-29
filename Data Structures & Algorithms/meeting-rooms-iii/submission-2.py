class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        available = list(range(n))
        heapq.heapify(available)
        
        occupied = []  # (end_time, room)
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # 释放房间
            while occupied and occupied[0][0] <= start:
                t, room = heapq.heappop(occupied)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (start + duration, room))
            else:
                t, room = heapq.heappop(occupied)
                heapq.heappush(occupied, (t + duration, room))
            
            count[room] += 1
        
        return count.index(max(count))
            

