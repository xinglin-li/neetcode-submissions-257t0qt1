class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 按会议开始时间排序
        meetings.sort(key=lambda x: x[0])

        # available_rooms 存储空闲房间号, 堆顶保证是编号最小的房间
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        # busy_rooms 存储 -> (结束时间, 房间ID), 堆顶保证是最早结束的会议
        busy_rooms = []
        
        count = [0]*n

        for start, end in meetings:
            # 1. 释放所有END <= 当前 START的房间
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room_id = heapq.heappop(busy_rooms)
                heapq.heappush(available_rooms, room_id)
            
            # 2. 如果有空闲房间, 把编号最小的房间分配出去
            if available_rooms:
                room_id = heapq.heappop(available_rooms)
                heapq.heappush(busy_rooms, (end, room_id))
            
            # 3. 没有空房, 排队等待最早房间结束
            else:
                earlist_end, room_id = heapq.heappop(busy_rooms)
                duration = end - start
                heapq.heappush(busy_rooms, (earlist_end + duration, room_id))
            
            count[room_id] += 1
        
        return count.index(max(count))