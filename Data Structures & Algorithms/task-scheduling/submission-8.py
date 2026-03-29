from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-freq for freq in count.values()]
        heapq.heapify(max_heap)

        q = deque() #[remaining_count, available_time]
        time = 0

        while max_heap or q:
            time += 1

            if max_heap:
                freq = 1 + heapq.heappop(max_heap) # since it is negative number, so +1
                if freq != 0:
                    q.append((freq, time + n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time
        