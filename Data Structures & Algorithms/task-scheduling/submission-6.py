class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use heap and queue to simulate the scheduler
        from collections import Counter, deque
        import heapq
        freq = collections.Counter(tasks)
        
        # max heap (Python heap is min-heap so store negative)
        maxheap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxheap)
        
        time = 0
        cooldown = deque()  # (ready_time, -remaining_count)
        
        while maxheap or cooldown:
            time += 1
            
            # 1. 执行一个任务
            if maxheap:
                cnt = heapq.heappop(maxheap) + 1  # +1 because cnt is negative
                if cnt != 0:
                    # 任务还有剩余次数，进入 cooldown
                    cooldown.append((time + n, cnt))
            
            # 2. 冷却完成的任务重新入堆
            if cooldown and cooldown[0][0] == time:
                ready_time, cnt = cooldown.popleft()
                heapq.heappush(maxheap, cnt)
        
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