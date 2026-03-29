class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        heap = []
        cur = 0
        for p, start, end in trips:
            # Get out of the car
            while heap and heap[0][0] <= start:
                e, pp = heapq.heappop(heap)
                cur -= pp
            # Get in the car
            cur += p
            if cur > capacity:
                return False
            heapq.heappush(heap, (end, p))
        return True