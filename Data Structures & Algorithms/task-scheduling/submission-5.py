class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use heap and queue to simulate the scheduler
        from collections import Counter, deque
        import heapq
        freq = Counter(tasks)
        maxheap = [-v for v in freq.values()]
        heapq.heapify(maxheap)
        time =0 
        cooldown = deque() # we need queue since the first in task will finish cooling down first
        while maxheap or cooldown:
            time += 1
            if maxheap:
                cnt = heapq.heappop(maxheap) + 1
                if cnt != 0:
                    cooldown.append((time+n,cnt))
            if cooldown and cooldown[0][0] == time:
                readytime , cnt = cooldown.popleft()
                heapq.heappush(maxheap,cnt)
        return time

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # the best way is to use math
        # formula: max(len(tasks),(freq_max - 1)*(n+1) + k), k is the number of tasks with freq equals freq_max
        from collections import Counter
        freq = Counter(tasks)
        freq_max = max(freq.values())
        k = sum(1 for val in freq.values() if val == freq_max)
        return max(len(tasks),(freq_max - 1)*(n+1) + k)
"""