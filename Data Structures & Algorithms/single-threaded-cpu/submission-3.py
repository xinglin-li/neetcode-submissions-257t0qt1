import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        # 加 index
        tasks = [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        tasks.sort()  # 按 enqueueTime 排序

        res = []
        heap = []

        time = 0
        i = 0

        while heap or i < n:
            # 如果没有任务可以处理，时间跳到下一个任务
            if not heap:
                time = max(time, tasks[i][0])

            # 把所有已经到达的任务加入 heap
            while i < n and tasks[i][0] <= time:
                enqueue, process, idx = tasks[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            # 处理一个任务
            process, idx = heapq.heappop(heap)
            time += process
            res.append(idx)

        return res
        
