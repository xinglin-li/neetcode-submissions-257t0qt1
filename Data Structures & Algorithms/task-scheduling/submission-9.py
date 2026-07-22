class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. 统计频次
        counts = Counter(tasks)
        
        # 2. 构建最大堆（Python 存负数）
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)
        
        # 3. 冷却队列：存储 (剩余频次负值, 可再次执行的时间)
        cooldown_queue = deque()
        
        time = 0
        
        # 只要堆里还有可以执行的任务，或者队列里还有等待冷却的任务，就继续循环
        while max_heap or cooldown_queue:
            time += 1
            
            # 检查是否有任务已经冷却完毕，可以重新放回堆中
            if cooldown_queue and cooldown_queue[0][1] == time:
                cnt, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, cnt)
                
            # 如果当前有可执行的任务，优先执行频次最高的
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # 执行一次，剩余次数 -1（因为存的是负值，所以加 1）
                if cnt < 0:
                    # 还需要再次执行，推入冷却队列，下一次可用时间为 time + n + 1
                    cooldown_queue.append((cnt, time + n + 1))
                    
            # 如果 max_heap 为空，这一轮 CPU 相当于经历了 1 个单位的 idle（time 正常 +1 即可）
            
        return time