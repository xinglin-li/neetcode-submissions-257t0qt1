class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        h = [(start, end, cap) for cap, start, end in trips]
        heapq.heapify(h)
        cur_cap = 0
        h_incar = []
        while h:
            start, end, cap = heapq.heappop(h)
            cur_cap += cap
            while h_incar:
                end_i, cap_i = heapq.heappop(h_incar)
                if end_i <= start:
                    cur_cap -= cap_i
                else:
                    heapq.heappush(h_incar,(end_i,cap_i))
                    break
            if cur_cap <= capacity:
                heapq.heappush(h_incar, (end,cap))
            else:
                return False
        return True
