class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 按 start 时间排序
        meetings.sort()

        # 空闲房间：按 room id
        free = list(range(n))
        heapq.heapify(free)

        # 占用房间：(end_time, room_id)
        busy = []

        # 每个房间使用次数
        count = [0] * n

        for start, end in meetings:
            duration = end - start

            # 释放所有在 start 之前结束的房间
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)

            if free:
                # 有空房
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
            else:
                # 没空房 → 延迟
                end_time, room = heapq.heappop(busy)
                new_end = end_time + duration
                heapq.heappush(busy, (new_end, room))

            count[room] += 1

        # 返回使用次数最多、编号最小的房间
        return count.index(max(count))