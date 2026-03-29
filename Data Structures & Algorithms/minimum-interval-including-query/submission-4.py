class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        import heapq

        # 按 interval 的起点排序
        intervals.sort()
        # 把 query 和原 index 绑定在一起
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        res = [-1] * len(queries)
        heap = []  # (length, right, left)
        i = 0      # 指向 intervals
        
        for q, idx in sorted_queries:
            # 把所有左端 <= q 的 interval 加入 heap
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                length = r - l + 1
                if r >= q:
                    heapq.heappush(heap, (length, r, l))
                i += 1
            
            # 清理右端 < q 的 interval
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            # heap 顶端即最短区间
            if heap:
                res[idx] = heap[0][0]
        
        return res