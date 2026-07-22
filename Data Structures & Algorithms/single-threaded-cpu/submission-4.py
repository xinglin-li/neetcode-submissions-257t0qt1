class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # 1. 附带原始索引，并按 enqueueTime 升序排序
        # 存储格式: [enqueueTime, processingTime, index]
        ext_tasks = sorted([(task[0], task[1], i) for i, task in enumerate(tasks)])
        
        min_heap = []
        res = []
        curr_time = 0
        i = 0
        n = len(tasks)
        
        # 当还有未处理的任务（未入堆或在堆中）时继续
        while i < n or min_heap:
            # 如果堆为空，且当前时间落后于下一个任务的到达时间，CPU 空闲，直接快进时间
            if not min_heap and curr_time < ext_tasks[i][0]:
                curr_time = ext_tasks[i][0]
                
            # 将所有 enqueueTime <= curr_time 的任务推入堆中
            while i < n and ext_tasks[i][0] <= curr_time:
                enqueue_time, process_time, original_idx = ext_tasks[i]
                # 堆按照 (processingTime, original_index) 排序
                heapq.heappush(min_heap, (process_time, original_idx))
                i += 1
                
            # 弹出堆顶（执行时间最短 / 索引最小）的任务
            process_time, original_idx = heapq.heappop(min_heap)
            res.append(original_idx)
            curr_time += process_time  # 累加 CPU 执行时间
            
        return res