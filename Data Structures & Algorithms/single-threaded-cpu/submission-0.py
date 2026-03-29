class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        arr = [(t[0],t[1],i) for i, t in enumerate(tasks)]
        arr.sort()
        res = []
        minHeap = []
        n = len(tasks)
        i = 0
        t = 1
        while i < n or minHeap:
            if not minHeap and t < arr[i][0]:
                t = arr[i][0]
            while i < n and t >= arr[i][0]:
                enqueueTime, processingTime, idx = arr[i]
                heapq.heappush(minHeap,(processingTime,idx))
                i += 1
            
            processingTime, idx = heapq.heappop(minHeap)
            t += processingTime
            res.append(idx)
        return res