class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = list(range(n))
        heapq.heapify(free)
        # busy: (end_time, room_id)
        busy = []
        count = [0]*n
        for start, end in meetings:
            duration = end - start
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)
            
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy,(end,room))
            else:
                end_time, room = heapq.heappop(busy)
                new_end = end_time + duration
                heapq.heappush(busy, (new_end, room))
            count[room] += 1
        
        return count.index(max(count))