class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])

        # 保存查询值和原始索引, 并对查询值从小到大排序 (离线处理)
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        res = [-1] * len(queries)
        min_heap = [] # (right - left + 1, right)
        i = 0
        n = len(intervals)

        for q, original_idx in sorted_queries:
            # 1. 把所有左端点 <= q 的区间入堆
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                length = r - l + 1
                heapq.heappush(min_heap, (length, r))
                i += 1
            # 2. 弹出堆顶, 所有right < q 的无效区间
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            # 3. 此时堆顶, 长度即为答案
            if min_heap:
                res[original_idx] = min_heap[0][0]
        return res