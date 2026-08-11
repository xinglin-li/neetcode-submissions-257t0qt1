class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. 统计每个任务的频次
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap) # 存可执行任务的负cnt

        # 冷却队列, (剩余负频次, 可以被重新调度的时刻)
        q = deque()
        time = 0
        
        # 只要堆里有可调度任务，或队列里有冷却中的任务，CPU 就在运行
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    # 未完成的任务放入冷却队列, 解冻时间为当前时间 + n
                    q.append((cnt, time + n))
            
            # 检查冷却队列是否有任务到了解冻时刻
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time
