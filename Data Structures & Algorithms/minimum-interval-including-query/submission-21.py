class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 离线查询（Offline Queries）+ 最小堆
        intervals.sort(key=lambda x: x[0])

        # 保存查询值和原始索引, 并对查询值从小到大排序 (离线处理)
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        res = [-1] * len(queries)
        min_heap = [] # (right - left + 1, right), 左端点小于q的会被推入堆中; 找长度最小, 并且有端点大于q的区间.
        i = 0
        n = len(intervals)

        for q, original_idx in sorted_queries:
            # 1. 把所有左端点 <= q 的区间入堆
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                if r >= q: # 仅能作为局部微优化，避免把当期已死区间推入堆
                    heapq.heappush(min_heap, (r - l + 1, r))
                i += 1
            # 2. 弹出堆顶, 所有right < q 的无效区间
            # 依然必须保留：清理之前查询遗留在堆中、对当前 q 已过期的区间
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            # 3. 此时堆顶, 长度即为答案
            if min_heap:
                res[original_idx] = min_heap[0][0]
        return res