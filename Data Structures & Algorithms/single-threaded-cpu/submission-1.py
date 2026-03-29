class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Step 1: 记录原始index，并按enqueue排序
        arr = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        arr.sort()  # sort by enqueueTime

        res = []
        h = []
        i = 0
        t = 0
        n = len(arr)

        while i < n or h:
            # CPU idle: jump time
            if not h and t < arr[i][0]:
                t = arr[i][0]

            # 所有当前时刻可加入的任务推到堆
            while i < n and arr[i][0] <= t:
                enqueue, proc, idx = arr[i]
                heapq.heappush(h, (proc, idx))
                i += 1

            # 处理一个任务
            proc, idx = heapq.heappop(h)
            t += proc
            res.append(idx)

        return res