class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        import heapq
        res = [-1]*len(queries)
        sorted_queries = sorted([(q,idx) for idx, q in enumerate(queries)])
        intervals.sort()
        heap = []
        i = 0

        for q, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                i += 1
                if right >= q:
                    length = right - left + 1
                    heapq.heappush(heap, (length, right))
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            if heap:
                res[idx] = heap[0][0]
        return res


